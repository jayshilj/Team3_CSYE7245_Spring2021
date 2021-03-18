#### Lab 2 - Machine Learning on Google Cloud Platform with Structured Data Pipelines

1. Google Docs Link : https://docs.google.com/document/d/1nZp3-RFUFJ-uLq3bbTdhCAqf9Am6QXLGCMuxSJFUorw/edit?usp=sharing

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1nZp3-RFUFJ-uLq3bbTdhCAqf9Am6QXLGCMuxSJFUorw#1

# CSYE7245 Big Data Systems & Intelligence Analytics Labs - Spring 2021
## Lab GCP - Machine Learning with structured Data 


### Requirements

- This lab requires an GCP account to deploy and run. Signup for an GCP Account [here](https://cloud.google.com/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1009892&utm_content=text-ad-none-any-DEV_c-CRE_491414383178-ADGP_Desk%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP%20~%20General_GCP-KWID_43700060017842318-kwd-527294293847&utm_term=KW_gcp%20account-ST_gcp%20account&gclid=Cj0KCQiAst2BBhDJARIsAGo2ldVk32gUHT8-jJgqiXElutyio2mSVM3nnaYCoqOjU6AIHFq-ZWaonrYaAsU0EALw_wcB).

- Python 3.7+


### Setup

#### GCP Signup & Configuration 

### Introduction: 
In this lab, we target to explore a structured dataset and then create training and evaluation datasets for a machine learning (ML) model. 

Key Architecture components:
We use the following architecture components: 

Data Exploration:  Google Cloud services Datalab for data exploration 
Data set creation:  Dataflow to create your datasets.
Data Storage: The source dataset is stored in BigQuery.
Application Workflow:


### Objective : 
Explore a public dataset with Datalab.
Execute queries to collect sample data from the Natality dataset,a public data set from the USA's Centers for Disease Control and Prevention (CDC) that is stored in BigQuery.
Identify features to use in your ML model.
Visualize the data using the Python data analysis tool Pandas. The Pandas dataframe is an in-memory data structure you can use for statistical calculations and data visualization.
Split the data into training and evaluation data files using Dataflow.
Launch a preprocessing pipeline using Dataflow to create training and evaluation datasets.
 
### Costs :
This tutorial uses billable components of Google Cloud, including:
Compute Engine
Dataflow
Cloud Storage
BigQuery
The estimated price to run this part of the tutorial, assuming you use every resource for an entire day, is approximately $1.45, based on this pricing calculator.



### Results : 
We can find the running job by using the Dataflow page in the Google Cloud Console.
We will find two pipelines, one that includes the training set, and the other that includes the evaluation set. 

The process typically takes about 30 minutes to finish, but might vary depending on the setup.
The following diagram shows the Dataflow data processing pipeline:


Find the CSV files for evaluation and training
The job creates multiple CSV files for both sets. Here are the first CSV files for the evaluation set and the training set:
gs://${BUCKET}/babyweight/preproc/eval.csv-00000-of-00016
gs://${BUCKET}/babyweight/preproc/train.csv-00000-of-00040

Reviewing the CSV files
Use the Cloud Storage page in the Google Cloud Console to see the entire set of files in the babyweight/preproc directory in your bucket.






