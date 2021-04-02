# -*- coding: utf-8 -*-

# http://localtest.me:8000
# http://localtest.me:8000/documentation
# http://localtest.me:8000/documentation?access_token=1234567asdfgh
# http://localtest.me:8000/logout 

import random
import string
from os import listdir
from os.path import isfile, join
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import random
from time import time
from decimal import Decimal
import boto3
import string
import random
import os
import os
import re
import collections
import nltk
import pandas as pd
from io import StringIO # python3; python2: BytesIO 
import os
import requests as requests
import json
import pandas as pd
import numpy as np
import snowflake.connector as sf
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 100)
from snowflake.connector.pandas_tools import write_pandas
from pandas import DataFrame
import h5py
import glob
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse

#################### FAST API  ###############################33

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
COOKIE_DOMAIN = "localtest.me"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)

# Generating a Random Token for API Key
letters = string.ascii_lowercase
tok = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
 

print('######################## YOUR UNIQUE TOKEN ######################')
print(tok)
API_KEY = tok


async def get_api_key(
        api_key_query: str = Security(api_key_query),
        api_key_header: str = Security(api_key_header),
        api_key_cookie: str = Security(api_key_cookie),
    ):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/")
async def homepage():
    return "Welcome to CNC Mill APIs Homepage"


@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = JSONResponse(
        get_openapi(title="FastAPI security test", version=1, routes=app.routes)
    )
    return response


@app.get("/documentation", tags=["documentation"])
async def get_documentation(api_key: APIKey = Depends(get_api_key)):
    response = get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
    #response = get_swagger_ui_html(openapi_url="/cnc/{experiment}/{process}", title="docs")
    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        domain=COOKIE_DOMAIN,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response

@app.get("/logout")
async def route_logout_and_remove_cookie():
    response = RedirectResponse(url="/")
    response.delete_cookie(API_KEY_NAME, domain=COOKIE_DOMAIN)
    return response


@app.get("/secure_endpoint", tags=["test"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = "URL has been authenticated"
    return response

#app = FastAPI()

class Item(BaseModel):
    experiment: int
    process: str
    condition: str
    columns: str
    data: str
    toolcondition: str
    passvisual: str
    machiningfinalized: str

@app.get("/getexpcnc/{experiment}", tags=["GET DATASET AS PER EXPERIMENT NUMBER"])
# async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    
def connecttosnowflake(experiment:int):
    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''select * from COMBINED_CNC_DATA where EXP_NO = %s''',(experiment))
    row_headers=[x[0] for x in cs.description] #this will extract row headers
    rv = cs.fetchall()
    print(rv)
    json_data=[]
    for result in rv:
        print(result)
        json_data.append(dict(zip(row_headers,result)))
    
    return json.dumps(json_data)

@app.get("/getunique/{columns}", tags=["GET UNIQUE VALUES FOR COLUMNS"])
# async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):

def querydata(columns: str):
    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''SELECT DISTINCT {} FROM COMBINED_CNC_DATA'''.format(columns))
    df = cs.fetch_pandas_all()
    print("THIS IS DF")
    print(df)  
    return df



@app.get("/getexperimentdatamachine/{experiment}/{process}", tags=["GET WHOLE DATASET AS PER EXPERIMENT & MACHINING_PROCESS"])
# async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    
def connecttosnowflake(experiment:int, process: str):
    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''select * from EXPERIMENT where EXP_NO = %s and MACHINING_PROCESS = %s ''',(experiment,process))
    row_headers=[x[0] for x in cs.description] #this will extract row headers
    rv = cs.fetchall()
    print(rv)
    json_data=[]
    for result in rv:
        print(result)
        json_data.append(dict(zip(row_headers,result)))
    
    return json.dumps(json_data)
  
@app.get("/knowexpwornstatus/{wornstatus}", tags=["KNOW EXPERIMENTS THAT FALLS UNDER TOOL CONDITION: WORN OR UNWORN"])

def querydata(wornstatus: str):

    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''SELECT DISTINCT EXP_NO FROM COMBINED_CNC_DATA WHERE TOOL_CONDITION=%s''',(wornstatus))
    rv = cs.fetchall()
    print(rv)
    return json.dumps(rv)


@app.get("/getdatatool/{toolcondition}", tags=["GET WHOLE DATA SET AS PER TOOL CONDITION: WORN OR UNWORN"])
# async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):

def querydata(toolcondition: str):
    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''SELECT * FROM COMBINED_CNC_DATA WHERE TOOL_CONDITION=%s''',(toolcondition))
    row_headers=[x[0] for x in cs.description] #this will extract row headers
    rv = cs.fetchall()
    print(rv)
    json_data=[]
    for result in rv:
        print(result)
        json_data.append(dict(zip(row_headers,result)))

    return json.dumps(json_data)


@app.get("/knowexppassvisual/{passvisual}", tags=["KNOW EXPERIMENTS THAT PASS VISUAL INSPECTION: YES OR NO"])
# async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):

def querydata(passvisual: str):

    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''SELECT DISTINCT EXP_NO FROM COMBINED_CNC_DATA WHERE PASSED_VISUAL_INSPECTION=%s''',(passvisual))
    rv = cs.fetchall()
    print(rv)
    return json.dumps(rv)

@app.get("/getdatavisualinspection/{passvisual}", tags=["GET WHOLE DATASET AS PER VISUAL INSPECTION: YES OR NO"])
    
def connecttosnowflake(passvisual: str):
    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''select * from COMBINED_CNC_DATA where PASSED_VISUAL_INSPECTION = %s ''',(passvisual))
    row_headers=[x[0] for x in cs.description] #this will extract row headers
    rv = cs.fetchall()
    print(rv)
    json_data=[]
    for result in rv:
        print(result)
        json_data.append(dict(zip(row_headers,result)))
    
    return json.dumps(json_data)


@app.get("/knowexpmachiningfinalized/{machiningfinalized}", tags=["KNOW EXPERIMENTS THAT PASS MACHINING FINALIZED: YES OR NO"])

def querydata(machiningfinalized: str):

    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''SELECT DISTINCT EXP_NO FROM COMBINED_CNC_DATA WHERE MACHINING_FINALIZED=%s''',(machiningfinalized))
    rv = cs.fetchall()
    print(rv)
    return json.dumps(rv)

@app.get("/getdatamachiningfinalized/{machiningfinalized}", tags=["GET WHOLE DATA THAT PASSED MACHINING_FINALIZED: YES OR NO"])
    
def connecttosnowflake(machiningfinalized: str):
    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()
    print ("connection successful")
    cs.execute('''USE CNC_MILL_TOOL_WEAR''')
    cs.execute('''select * from COMBINED_CNC_DATA where MACHINING_FINALIZED = %s''',(machiningfinalized))
    row_headers=[x[0] for x in cs.description] #this will extract row headers
    rv = cs.fetchall()
    print(rv)
    json_data=[]
    for result in rv:
        print(result)
        json_data.append(dict(zip(row_headers,result)))
    
    return json.dumps(json_data)


if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='0.0.0.0')