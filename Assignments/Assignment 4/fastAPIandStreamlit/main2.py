#Core Packages
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field   
from bs4 import BeautifulSoup
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from fastapi import FastAPI
import json
import boto3
import requests,datetime
import time
from random import randint
import urllib.request
import logging
import threading
import sys
import logging
import threading
import sys
from botocore.vendored import requests
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from mangum import Mangum
from fastapi_cloudauth.cognito import Cognito, CognitoCurrentUser, CognitoClaims
from boto3.dynamodb.conditions import Key
verified = "False"
import requests as requests


data_dir = '/root/Assignment4/Assignment-Trial/Assignment-Trial/inference-data/'
data_dir2 = '/root/Assignment4/Assignment-Trial/Assignment-Trial/fastAPIandStreamlit/awsdownload/'
data_dir3 = '/root/Assignment4/Assignment-Trial/Assignment-Trial/fastAPIandStreamlit/awsdownloadstar/'

ACCESS_KEY_ID = 'AKIA5CUSOFRV36GAHXEX'
ACCESS_SECRET_KEY = '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'

import boto3
dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=ACCESS_KEY_ID,
                    aws_secret_access_key=ACCESS_SECRET_KEY,
                    aws_session_token='None')

#init app
app = FastAPI(title="Deidentification System",
              description='''API to call from the recommendAPI''',
              version="0.1.0",)

# @app.get("/scrap")
# # def scrapeData(enterurl: str,verified: str):
# def scrapeData(enterurl: str):
#     def grab_page(url,url_ending):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
#         'Connection' : 'keep-alive',
#         'Content-Length' : '799',
#         'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
#         'accept': '/',
#         'sec-fetch-site': 'cross-site',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-dest': 'empty',
#         'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8,hi;q=0.7,mr;q=0.6'
#         }
#         page = requests.get(url + "/", headers = headers, timeout=5)
#         page_html = page.text
#         soup = BeautifulSoup(page_html, 'html.parser')
#         meta = soup.find("div",{'class':'a-info get-alerts'})
#         content = soup.find(id="a-body")
#         text = content.text
#         s3 = boto3.resource('s3')
#         s3.Object('inputpii', 'abc' + str(randint(0,100))+'.txt').put(Body=text)

#     def process_list_page(k):
#         #origin_page = "http://seekingalpha.com/earnings/earnings-call-transcripts" + "/" + str(k)
#         origin_page = userurl + "/" + str(k)
#         #print("getting page " + origin_page)
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
#         page = requests.get(origin_page, headers = headers)
#         page_html = page.text
#         #print(page_html)
#         soup = BeautifulSoup(page_html, 'html.parser')
#         alist = soup.find_all("li",{'class':'list-group-item article'})
#         for i in range(0,len(alist)):
#             url_ending = alist[i].find_all("a")[0].attrs['href']
#             url = "http://seekingalpha.com" + url_ending
#             #print(url)
#             #print(url_ending)
#             grab_page(url,url_ending)
#             #print(url)
#             time.sleep(.5)
            
#    # if ver
#     for i in range(1,1): #choose what pages of earnings to scrape
#         process_list_page(i,enterurl)
    
#     return {
#         #'statusCode': 200,
#         'body': json.dumps('Successful')}

# @app.get("/displayscrapdata")
# def scrapdatadisplay():

#     s3 = boto3.client("s3")
#     bucket = "inputpii"
#     key = "abcde.txt"
#     file = s3.get_object(Bucket=bucket, Key=key)
#     paragraph = str(file['Body'].read())
   
#     return {
       
#         'body': json.dumps(paragraph)
#     }

# @app.get("/identifyEntity")
# def identifyPIIEntity(verified):
#     print(verified)
#     if(verified == "True"):
#         s3 = boto3.client("s3")
#         bucket = "inputpii"
#         key = "abcde.txt"
#         file = s3.get_object(Bucket=bucket, Key=key)
#         paragraph = str(file['Body'].read())
  
#         comprehend = boto3.client("comprehend")
    
#         entities = comprehend.detect_entities(Text=paragraph, LanguageCode = "en")
#         keyphrase = comprehend.detect_key_phrases(Text=paragraph, LanguageCode = "en")

#         s3 = boto3.resource('s3')
#         BUCKET_NAME = "outputpii"

#         OUTPUT_NAME = f"dataKeyTest.json"
#         OUTPUT_BODY = json.dumps(entities)
#         s3.Bucket(BUCKET_NAME).put_object(Key=OUTPUT_NAME, Body=OUTPUT_BODY)

#         return {
        
#             'body': json.dumps(entities)
#         }

#     else:
#         return{
#             'body': json.dumps('Authenticate User')
#         }

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String
    Args:
      text_content The text content to analyze
    """
    #global df_sentimentScore 
    # global sentiment_score
    # global sentiment_magnitude
    # global sentence1
    # global langue
    # #print(text_content)
    # client = language_v1.LanguageServiceClient()
    # # text_content = 'I am so happy and joyful.'
    # # Available types: PLAIN_TEXT, HTML
    # type_ = language_v1.Document.Type.PLAIN_TEXT
    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    # language = "en"
    # document = {"content": text_content, "type_": type_, "language": language}
    # # Available values: NONE, UTF8, UTF16, UTF32
    # encoding_type = language_v1.EncodingType.UTF8
    # response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    #print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    #response = 
    # import requests

    # datatosend = {"text": "Hello we are good"}
    # send = requests.post("http://0.0.0.0:8888/predict", data=datatosend)

    # print(send.content)


def sentiment_main(passed_list):
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--text_content", type=str, default=["I am so happy and joyful.","Ifyou are bad I'm your dada"])
    #args = parser.parse_args()
    #label_list=["I am so happy and joyful.","Ifyou are bad I'm your dada","I am so happy and joyful.","Ifyou are bad I'm your dada"]
    #remove_stopwords()
    #processed_list=processed_list[0:5]
    count = 0
    for i in passed_list:
        #print(i)
        sample_analyze_sentiment(i)
        count = count + 1
        if count == 30:
            break




@app.get("/maskEntity")
def maskIdentifiedEntity(UserInput: str):
    with open(data_dir + UserInput) as f:
        text = f.read()
        temp_list= []
        #text = text[:4000]
        #x = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
        # st.text(x)
        #print("Hello")
        
        temp_list=text.split(".")
        #content_list=content_list+temp_list
        
        f.close()


        # x = []
        # y = []
        # count = 0
        # for i in temp_list:
            
        # #print(text_content)
        # #client = language_v1.LanguageServiceClient()
        # # text_content = 'I am so happy and joyful.'
        
        #     data = {
        #         "text": i   # json 
        #     }
        #     r = requests.post('http://0.0.0.0:8888/predict',json=data)
        #     print("Hit Successful")
        #     print(r.text)
        #     x.append(r.text)
        #     y.append(i)
        #     if count == 15:
        #         break
            
        #     count = count+1

        

        #print(temp_list)
    return {
        'body': text
    }
    # return {
     
    #     'body': r
    # }

@app.get("/display_mask_entity")
def get_mask_PII_entity(UserInput: str):
    #user_input = st.text_input("Enter the name of the Company")
    comprehend = boto3.client(service_name='comprehend',aws_access_key_id = 'AKIA5CUSOFRV64J75U7W', aws_secret_access_key = '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', region_name = 'us-east-1')
        #text = "Good afternoon, everyone and welcome to NIKE"
    with open(data_dir + UserInput) as f:
        text = f.read()
        text = text[:4000]
        x = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
        #st.text(x)
        
   
    return {
        #'statusCode': 200,
        'body': json.dumps(x)
    }

@app.get("/replacePIIEntity")
def replacewithPIIEntity(UserInput: str):
    
    UserInput = UserInput+".out"
    time.sleep(1.4)
    try:
        with open(data_dir2 + UserInput) as f:
            #st.text(f.read())
            x = f.read()
    except:
        print("Company Does not Exist")
    return {
        'statusCode': 200,
        'body': json.dumps(x)
    }

@app.get("/displayPIIEntitywithStar")
def get_mask_PII_entity(UserInput: str):
    UserInput = UserInput +".out"
    time.sleep(1.4)

    try:
        with open(data_dir3 + UserInput) as f:
            # st.text(f.read())
            x = f.read()
    except:
        st.text("Company Does not Exist")
   
    return {
        #'statusCode': 200,
        'body': json.dumps(x)
    }


@app.get("/Authentication", tags=["Auth"])
async def userauthentication(usrName: str, usrPassword: str): 
    OTP = usrName + usrPassword
    
    # dynamodb = boto3.resource('dynamodb')
    
    # table = dynamodb.Table('users')
    # response = table.get_item(Key = {'login': OTP})
    dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=ACCESS_KEY_ID,
                    aws_secret_access_key=ACCESS_SECRET_KEY,
                    region_name='us-east-1')


    table = dynamodb.Table('users')

    response = table.scan()

    OTPD = response['Items']
    userlist = []
    i = 0
    while i < len(OTPD):
        #print(OTP[i])
        x = OTPD[i]['login']
        print(x)
        userlist.append(x)
        i=i+1

    #if OTP in userlist:


    if OTP in userlist :
        verified = "True"
        result = "Congratulations User Verified!!"
    else:
        verified = "False"
        result = "Please enter valid username/password!!"
        
    return result

#Deidentification generate HashMessage
@app.get("/Anonymize", tags=["Auth"])
async def deidentifyEntities(): 
    
    dynamodb = boto3.resource('dynamodb')
    dynamodbClient = boto3.client("dynamodb")
    table = dynamodb.Table('DeidentificationLookUpTable')
    Hash = 'c16e783f3dec14e234b1969b07af869de846f99f6a53df1954017b7779915ecb'
    fileName = str('deidentifiedmessage')

    s3 = boto3.client("s3")
    bucket = "outputpii"
    key = fileName + ".txt"
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())
  

    return {
     
        'body': json.dumps(paragraph)
    }


    ##View Deidentified
@app.get("/deanonymize", tags=["Auth"])
async def deidentifyEntities(user_input: str): 
    #user_input = "AGEN"
    with open(data_dir + user_input) as f:
        text = f.read()
        #text = text[:4000]
        #x = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
        # st.text(x)
        #print("Hello")

    return {
     
        'body': json.dumps(text)
    }

@app.get("/sentiment", tags=["Sentimental Analysis"])
async def deidentifyEntities(UserInput: str): 
    #user_input = "AGEN"
    UserInput = UserInput +".out"
    time.sleep(1.4)
    with open(data_dir3 + UserInput) as f:
        
        text = f.read()

        temp_list= []
        #text = text[:4000]
        #x = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
        # st.text(x)
        #print("Hello")
        
        temp_list=text.split(".")

        #text = text[:4000]
        #x = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
        # st.text(x)
        #print("Hello")
        x = []
        y = []
        count = 0
        for i in temp_list:
            
        #print(text_content)
        #client = language_v1.LanguageServiceClient()
        # text_content = 'I am so happy and joyful.'
        
            data = {
                "text": i   # json 
            }
            r = requests.post('http://0.0.0.0:8888/predict',json=data)
            print("Hit Successful")
            print(r.text)
            x.append(r.text)
            y.append(i)
            if count == 15:
                break
            
            count = count+1
        #print(temp_list)
    return {
        'Sentence': y,
        'sentiment': x
    }
