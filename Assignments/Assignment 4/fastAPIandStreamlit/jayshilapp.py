import streamlit as st
import altair as alt
from os import listdir
from os.path import isfile, join
from pydantic import BaseModel
import boto3
import json
import time
import pandas as pd
import yfinance as yf
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import string
from datetime import datetime
import requests as requests

data_dir = '/root/Assignment4/Assignment-Trial/Assignment-Trial/inference-data/'
data_dir2 = '/root/Assignment4/Assignment-Trial/Assignment-Trial/fastAPIandStreamlit/awsdownload/'
data_dir3 = '/root/Assignment4/Assignment-Trial/Assignment-Trial/fastAPIandStreamlit/awsdownloadstar/'

companies = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]
@st.cache
def load_data():
    #df = data.cars()
    return 0

def get_data(company: str, year: int):
    if company in companies and year == 2021:
        with open(data_dir + company) as f:
            s = f.read()
        return {"company": company, "transcript": s}
    else:
        raise HTTPException(status_code=404, detail="Company not found")

def get_data(company: str, year: int):
    if company in companies and year == 2021:
        with open(data_dir + company) as f:
            s = f.read()
        return {"company": company, "transcript": s}
    else:
        raise HTTPException(status_code=404, detail="Company not found")



def main():
    df = load_data()

    
    page = st.sidebar.radio("Choose a page", ["Homepage", "SignUp"])
    if page == "Homepage":

        ACCESS_KEY_ID = 'xxx'
        ACCESS_SECRET_KEY = 'xxx'
        st.title('** Welcome to Team 3 CSYE !!!**')
        st.header('User Authentication')

        st.subheader('Please enter valid username password and Acess Token')
    
        usrName = st.text_input('Username')
        usrPassword = st.text_input('Password')
        acesstoken = st.text_input('Enter your Token')

        OTP = usrName + usrPassword
        dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=ACCESS_KEY_ID,
                    aws_secret_access_key=ACCESS_SECRET_KEY,
                    region_name='us-east-1')


        table = dynamodb.Table('users')

        response = table.scan()

        OTPD = response['Items']
        userlist = []
        toklist = []
        i = 0
        while i < len(OTPD):
            #print(OTP[i])
            x = OTPD[i]['login']
            y = OTPD[i]['acesstoken']
            #print(x)
            userlist.append(x)
            toklist.append(y)
            i=i+1

        

        
        if OTP in userlist and acesstoken in toklist :
            verified = "True"
            result = "Congratulations User Verified!!"
            page = st.sidebar.radio("Choose a page", ["Text_File", "AWS Comprehend","PII Masked Data","Star Masked Data","Fundamental" ,"Technical","Sentiment"])
            st.title(result)
            
            if page == "Text_File":
                st.title("Text File Reader")
                #st.text_input('Enter the name of the Company')
                user_input = st.text_input("Enter the name of the Company")
                try:
                    with open(data_dir + user_input) as f:
                        st.text(f.read())
                except:
                    st.text("Company Does not Exist")
            elif page == "AWS Comprehend":
                st.title("Text File Reader")
                #st.text_input('Enter the name of the Company')
                user_input = st.text_input("Enter the name of the Company")
                comprehend = boto3.client(service_name='comprehend',aws_access_key_id = 'AKIA5CUSOFRV64J75U7W', aws_secret_access_key = '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', region_name = 'us-east-1')
                    #text = "Good afternoon, everyone and welcome to NIKE"
                with open(data_dir + user_input) as f:
                    text = f.read()
                    text = text[:4000]
                    x = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
                    st.text(x)
                    print("Hello World")
            elif page == "PII Masked Data":
                st.title("Masked Data Using PII")
                user_input = st.text_input("Enter the name of the Company")
                user_input = user_input+".out"
                time.sleep(1.4)
                try:
                    with open(data_dir2 + user_input) as f:
                        st.text(f.read())
                except:
                    st.text("Company Does not Exist")
            
            elif page == "Star Masked Data":
                
                st.title("Star Data Using AWS Comprehend")
                user_input = st.text_input("Enter the name of the Company")
                user_input = user_input+".out"
                time.sleep(1.4)
            

                try:
                    with open(data_dir3 + user_input) as f:
                        st.text(f.read())
                except:
                    st.text("Company Does not Exist")
                
            elif page == "Sentiment":
                st.title("Sentiment Analysis for Masked Data")
                user_input = st.text_input("Enter the name of the Company")
                user_input = user_input+".out"

                with open(data_dir3 + user_input) as f:
                    text = f.read()

                    temp_list= []
            
                    temp_list=text.split(".")

                    x = []
                    y = []
                    count = 0
                    for i in temp_list:
                                          
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
                        st.text(x)
                        st.text(y)
                        
                        count = count+1

            
            

            elif page == "Technical":
                snp500 = pd.read_csv("/root/Assignment4/Assignment-Trial/Assignment-Trial/fastAPIandStreamlit/Trading-main/Datasets/SP500.csv")
                symbols = snp500['Symbol'].sort_values().tolist()   

                ticker = st.selectbox(
                    'Choose a S&P 500 Stock',
                symbols)

                stock = yf.Ticker(ticker)

                def calcMovingAverage(data, size):
                    df = data.copy()
                    df['sma'] = df['Adj Close'].rolling(size).mean()
                    df['ema'] = df['Adj Close'].ewm(span=size, min_periods=size).mean()
                    df.dropna(inplace=True)
                    return df
            
                def calc_macd(data):
                    df = data.copy()
                    df['ema12'] = df['Adj Close'].ewm(span=12, min_periods=12).mean()
                    df['ema26'] = df['Adj Close'].ewm(span=26, min_periods=26).mean()
                    df['macd'] = df['ema12'] - df['ema26']
                    df['signal'] = df['macd'].ewm(span=9, min_periods=9).mean()
                    df.dropna(inplace=True)
                    return df

                def calcBollinger(data, size):
                    df = data.copy()
                    df["sma"] = df['Adj Close'].rolling(size).mean()
                    df["bolu"] = df["sma"] + 2*df['Adj Close'].rolling(size).std(ddof=0) 
                    df["bold"] = df["sma"] - 2*df['Adj Close'].rolling(size).std(ddof=0) 
                    df["width"] = df["bolu"] - df["bold"]
                    df.dropna(inplace=True)
                    return df

                st.title('Technical Indicators')
                st.subheader('Moving Average')
                
                coMA1, coMA2 = st.beta_columns(2)
                
                with coMA1:
                    numYearMA = st.number_input('Insert period (Year): ', min_value=1, max_value=10, value=2, key=0)    
                
                with coMA2:
                    windowSizeMA = st.number_input('Window Size (Day): ', min_value=5, max_value=500, value=20, key=1)  
                    

                start = dt.datetime.today()-dt.timedelta(numYearMA * 365)
                end = dt.datetime.today()
                dataMA = yf.download(ticker,start,end)
                df_ma = calcMovingAverage(dataMA, windowSizeMA)
                df_ma = df_ma.reset_index()
                    
                figMA = go.Figure()
                
                figMA.add_trace(
                        go.Scatter(
                                x = df_ma['Date'],
                                y = df_ma['Adj Close'],
                                name = "Prices Over Last " + str(numYearMA) + " Year(s)"
                            )
                    )
                
                figMA.add_trace(
                            go.Scatter(
                                    x = df_ma['Date'],
                                    y = df_ma['sma'],
                                    name = "SMA" + str(windowSizeMA) + " Over Last " + str(numYearMA) + " Year(s)"
                                )
                        )
                
                figMA.add_trace(
                            go.Scatter(
                                    x = df_ma['Date'],
                                    y = df_ma['ema'],
                                    name = "EMA" + str(windowSizeMA) + " Over Last " + str(numYearMA) + " Year(s)"
                                )
                        )
                
                figMA.update_layout(legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01
                ))
                
                figMA.update_layout(legend_title_text='Trend')
                figMA.update_yaxes(tickprefix="$")
                
                st.plotly_chart(figMA, use_container_width=True)  
                
                st.subheader('Moving Average Convergence Divergence (MACD)')
                numYearMACD = st.number_input('Insert period (Year): ', min_value=1, max_value=10, value=2, key=2) 
                
                startMACD = dt.datetime.today()-dt.timedelta(numYearMACD * 365)
                endMACD = dt.datetime.today()
                dataMACD = yf.download(ticker,startMACD,endMACD)
                df_macd = calc_macd(dataMACD)
                df_macd = df_macd.reset_index()
                
                figMACD = make_subplots(rows=2, cols=1,
                                    shared_xaxes=True,
                                    vertical_spacing=0.01)
                
                figMACD.add_trace(
                        go.Scatter(
                                x = df_macd['Date'],
                                y = df_macd['Adj Close'],
                                name = "Prices Over Last " + str(numYearMACD) + " Year(s)"
                            ),
                        row=1, col=1
                    )
                
                figMACD.add_trace(
                        go.Scatter(
                                x = df_macd['Date'],
                                y = df_macd['ema12'],
                                name = "EMA 12 Over Last " + str(numYearMACD) + " Year(s)"
                            ),
                        row=1, col=1
                    )
                
                figMACD.add_trace(
                        go.Scatter(
                                x = df_macd['Date'],
                                y = df_macd['ema26'],
                                name = "EMA 26 Over Last " + str(numYearMACD) + " Year(s)"
                            ),
                        row=1, col=1
                    )
                
                figMACD.add_trace(
                        go.Scatter(
                                x = df_macd['Date'],
                                y = df_macd['macd'],
                                name = "MACD Line"
                            ),
                        row=2, col=1
                    )
                
                figMACD.add_trace(
                        go.Scatter(
                                x = df_macd['Date'],
                                y = df_macd['signal'],
                                name = "Signal Line"
                            ),
                        row=2, col=1
                    )
                
                figMACD.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1,
                    xanchor="left",
                    x=0
                ))
                
                figMACD.update_yaxes(tickprefix="$")
                st.plotly_chart(figMACD, use_container_width=True)
                
                st.subheader('Bollinger Band')
                coBoll1, coBoll2 = st.beta_columns(2)
                with coBoll1:
                    numYearBoll = st.number_input('Insert period (Year): ', min_value=1, max_value=10, value=2, key=6) 
                    
                with coBoll2:
                    windowSizeBoll = st.number_input('Window Size (Day): ', min_value=5, max_value=500, value=20, key=7)
                
                startBoll= dt.datetime.today()-dt.timedelta(numYearBoll * 365)
                endBoll = dt.datetime.today()
                dataBoll = yf.download(ticker,startBoll,endBoll)
                df_boll = calcBollinger(dataBoll, windowSizeBoll)
                df_boll = df_boll.reset_index()
                figBoll = go.Figure()
                figBoll.add_trace(
                        go.Scatter(
                                x = df_boll['Date'],
                                y = df_boll['bolu'],
                                name = "Upper Band"
                            )
                    )
                
                
                figBoll.add_trace(
                            go.Scatter(
                                    x = df_boll['Date'],
                                    y = df_boll['sma'],
                                    name = "SMA" + str(windowSizeBoll) + " Over Last " + str(numYearBoll) + " Year(s)"
                                )
                        )
                
                
                figBoll.add_trace(
                            go.Scatter(
                                    x = df_boll['Date'],
                                    y = df_boll['bold'],
                                    name = "Lower Band"
                                )
                        )
                
                figBoll.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1,
                    xanchor="left",
                    x=0
                ))
                
                figBoll.update_yaxes(tickprefix="$")
                st.plotly_chart(figBoll, use_container_width=True)

            elif page == "Fundamental":
                snp500 = pd.read_csv("/root/Assignment4/Assignment-Trial/Assignment-Trial/fastAPIandStreamlit/Trading-main/Datasets/SP500.csv")
                symbols = snp500['Symbol'].sort_values().tolist()   

                ticker = st.selectbox(
                    'Choose a S&P 500 Stock',
                symbols)

                stock = yf.Ticker(ticker)
                stock = yf.Ticker(ticker)
                info = stock.info 
                st.title('Company Profile')
                st.subheader(info['longName']) 
                st.markdown('** Sector **: ' + info['sector'])
                st.markdown('** Industry **: ' + info['industry'])
                st.markdown('** Phone **: ' + info['phone'])
                st.markdown('** Address **: ' + info['address1'] + ', ' + info['city'] + ', ' + info['zip'] + ', '  +  info['country'])
                st.markdown('** Website **: ' + info['website'])
                st.markdown('** Business Summary **')
                st.info(info['longBusinessSummary'])
                    
                fundInfo = {
                        'Enterprise Value (USD)': info['enterpriseValue'],
                        'Enterprise To Revenue Ratio': info['enterpriseToRevenue'],
                        'Enterprise To Ebitda Ratio': info['enterpriseToEbitda'],
                        'Net Income (USD)': info['netIncomeToCommon'],
                        'Profit Margin Ratio': info['profitMargins'],
                        'Forward PE Ratio': info['forwardPE'],
                        'PEG Ratio': info['pegRatio'],
                        'Price to Book Ratio': info['priceToBook'],
                        'Forward EPS (USD)': info['forwardEps'],
                        'Beta ': info['beta'],
                        'Book Value (USD)': info['bookValue'],
                        'Dividend Rate (%)': info['dividendRate'], 
                        'Dividend Yield (%)': info['dividendYield'],
                        'Five year Avg Dividend Yield (%)': info['fiveYearAvgDividendYield'],
                        'Payout Ratio': info['payoutRatio']
                    }
                
                fundDF = pd.DataFrame.from_dict(fundInfo, orient='index')
                fundDF = fundDF.rename(columns={0: 'Value'})
                st.subheader('Fundamental Info') 
                st.table(fundDF)
                
                st.subheader('General Stock Info') 
                st.markdown('** Market **: ' + info['market'])
                st.markdown('** Exchange **: ' + info['exchange'])
                st.markdown('** Quote Type **: ' + info['quoteType'])
                
                start = dt.datetime.today()-dt.timedelta(2 * 365)
                end = dt.datetime.today()
                df = yf.download(ticker,start,end)
                df = df.reset_index()
                fig = go.Figure(
                        data=go.Scatter(x=df['Date'], y=df['Adj Close'])
                    )
                fig.update_layout(
                    title={
                        'text': "Stock Prices Over Past Two Years",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'})
                st.plotly_chart(fig, use_container_width=True)
                
                marketInfo = {
                        "Volume": info['volume'],
                        "Average Volume": info['averageVolume'],
                        "Market Cap": info["marketCap"],
                        "Float Shares": info['floatShares'],
                        "Regular Market Price (USD)": info['regularMarketPrice'],
                        'Bid Size': info['bidSize'],
                        'Ask Size': info['askSize'],
                        "Share Short": info['sharesShort'],
                        'Short Ratio': info['shortRatio'],
                        'Share Outstanding': info['sharesOutstanding']
                
                    }
                
                marketDF = pd.DataFrame(data=marketInfo, index=[0])
                st.table(marketDF)
        else:
            verified = "False"
            result = "Please enter valid Username, Password and Acess Token!!"
    
            st.title(result)
    
    
    elif page == "SignUp":
            signusrName = st.text_input('Username')
            signusrPassword = st.text_input('Password')
            #signusrPasswordRepeat = st.text_input('Repeat Password')
            #accesstoken = st.text_input('Enter your Access Token')


            userOPT = signusrName + signusrPassword      
            
            ACCESS_KEY_ID = 'AKIA5CUSOFRV36GAHXEX'
            ACCESS_SECRET_KEY = 'V2S+FgynLZDJUTxDzlk6PIMl1hkSkhV/dUOOiinu'

# dynamodb = boto3.resource('dynamodb',region_name='REGION', ) 
            dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=ACCESS_KEY_ID,
                    aws_secret_access_key=ACCESS_SECRET_KEY,
                    region_name='us-east-1')


            dynamoTable = dynamodb.Table('users')

            # Generating a Random Token for API Key
            letters = string.ascii_lowercase
            tok = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(835))

            print('######################## YOUR UNIQUE TOKEN ######################')
            print(tok)
        

            # Code to Put the Item
            if signusrName == "" or signusrPassword == "":
                st.text('Please enter Valid Values')

            else:
                st.title('Congratulations, Your Account is created Successfully!')
                st.title('Your Unique Token from AWS Cognito: ')
                st.title(tok)
                dynamoTable.put_item(
                    Item={
                        'login': userOPT,
                        'acesstoken': tok
                    }
                )


            

if __name__ == "__main__":
    main()
