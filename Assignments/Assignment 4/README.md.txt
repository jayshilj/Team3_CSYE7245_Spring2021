# CSYE7245---Team-4---Big-Data-Sys-Int-Analytics-Master

## Assignment 4 - To deploy a sentiment analysis model to create a Model-as-a-service for anonymized data 

| NAME              |     NUID        |
|------------------ |-----------------|
| Akash Dubey       |   001302139     |
| Jayshil Jain      |   001300508     |
| Sagar Shah        |   001342989     |


1. Google Docs Link https://docs.google.com/document/d/125filBsknyMQXI_pVzSpPBoVPvsLhcdRCzsujmR5Uq4/edit#heading=h.1bu99q18iubo

2. CLAT Document Link : 

### About Data Masking, Anonymization and Deanonymization

Masking is hiding data with altered values like * or # or replacing it with PII entity type
Anonymization is used to prevent someone's personal identity from being revealed by generating it's MessageHash and EntityHash which can later be deanonymized using MessageHash

### Objectives

Who- Masking and Anonymization system can be used by companies in all sectors like Healthcare, Banking, Technology etc. whose customer data needs to be kept secure

What- To Scrap data, Identify PII entities from the scrapped data, perform masking and anonymization on the identified PII entities and Deanonymize the data 

Why- Personally Identified information identifies an individual's information which cannot be shared and needs to be kept private. Masking and anonymization would assist in securing individual's personal information and Deanonymization can retrieve the data as per requirements  

When -Over a 2 weeks period timeline

Where -This project will be delivered to the companies requiring to secure their customers personal information

How- Implemented scrapping, Identify PII entites, perform masking and anonymization and deanonymize the data and used technologies like Streamlit, FastAPI, AWSCloud.

## Available Scripts

In the project directory, you can run:

### `streamlit run streamlit_app.py`
Open [http://localhost:8501](http://localhost:8501) to view it in the browser.

Hot reloading will be enabled when in settings you will select 'run on save'.<br />

### `uvicorn main:app --reload`
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
Swagger UI page will be displayed where you can test your API's
![]()

### User Authentication 

![]()

#### API 1 : Scraping

![]()

#### API 2 : Named Entity Recognition 

![]()

#### API 3 Part 1: Implement masking

![]()

#### API 3 Part 2: Anonymization functions

#### API 4 : Deanonymization

![]() 







### About Sentiment Analysis

Sentiment Analysis is a process of determining the emotional tone behind a series of words, used to gain an understanding of the the attitudes, opinions and emotions expressed within an online mention.

Sentiment Analysis helps businesses understand how customers feel about their brand, giving them first-hand information to improve their products, make data-driven decisions, and deliver better customer experiences.

### Objectives

Who - Helps Data analysts within large organizations conduct market research, monitor brand and product reputation, and understand customer experiences.Analyzing the sentiment can be used by companies in various sectors to classify the sentence sentiment as positive, negative or neutral.

What - Train tensorflow model using AlBert, integrated trained model to fastaspi code to analyze the text files stored in S3, Dockerized the API service and built a streamlit application to access API service

Why - To understand sentiment of the text for customer review analysis, conduct market research and monitor reputation

When - Over one week period timeline

Where - This project will be delivered to companies requiring to analyze their data in order to develop better marketing strategies, improve customer satisfaction, to analyze which movies/tv series are doing well and getting better reviews etc.

How - Implemented tensorflow model(python), AWS cloud services, FastAPI, Docker and Streamlit

### 1.Train TensorFlow models using TensorFlow Extended (TFX) 

Followed the reference architectures : https://blog.tensorflow.org/2020/03/part-1-fast-scalable-and-accurate-nlp-tensorflow-deploying-bert.html

https://blog.tensorflow.org/2020/06/part-2-fast-scalable-and-accurate-nlp.html

Train the model for the anonymized data using BERT and this architecture that leverages TensorFlow Hub, Tensorflow Transform, TensorFlow Data Validation and Tensorflow Text and Tensorflow Serving 

### 2.Serve the model as a REST API 

Reference link: https://github.com/curiousily/Deploy-BERT-for-Sentiment-Analysis-with-FastAPI

##### Swagger UI 

##### Available Scripts

To run FastAPI code go to project directory:-

#### `uvicorn sentiment_analyzer.api:app`


### 3.Dockerize the API service. For sample code on how to Dockerize API

Building Docker Image:-

#### `docker build -t bertanalyzer .`

Running the image on Docker container

#### `docker run -i --name myapicontainer -p 8888:8888 bertanalyzer`

### 4.Build a Reference App in Streamlit to test the API

Reference link:- https://testdriven.io/blog/fastapi-streamlit/

##### Welcome Page

##### Analyze Sentiments

#### To run the streamlit app go to project directory:-

#### `streamlit run streamlit_app.py`

