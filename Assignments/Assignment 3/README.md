# CSYE7245 - Data as a Service API and Understanding Moody Analytics - Assignment 3
## Case Study:

Datalytics Inc. is interested in monetizing it’s data and making it’s data available as an API.They have invited our team to put together an application using Fast API to illustrate how it works. Datalytics Inc. reviewed multiple APIs available and were inspired by https://developer.moody's analytics.com/.

Who - Moody Analytics who have a large business user base provide secure API’s as per applications domain and functionality.

What - Perform Data ingestion Pipeline, Design Fast API, enable API key authentication and test the API implementation 

Why - To illustrate the value of  Data as a Service to generate API’s and ease user experience by providing API as per business requirements.

When - Over a 1 week period timeline. 

Where - This project will help business, leader's make better and faster decisions by making available API's as per their application's requirement. Providing interactive API will help enhance customer experience


## Report

https://codelabs-preview.appspot.com/?file_id=12V6OoxNlnM9nCU-i714cgh53a_2Iiz1lMqG3lm6gRy4#1


## Dataset overview: 

#### Context
A series of machining experiments were run on 2" x 2" x 1.5" wax blocks in a CNC milling machine in the System-level Manufacturing and Automation Research Testbed (SMART) at the University of Michigan. Machining data was collected from a CNC machine for variations of tool condition, feed rate, and clamping pressure. Each experiment produced a finished wax part with an "S" shape - S for smart manufacturing - carved into the top face, as shown in test_artifact.jpg (included in the dataset).

#### Content
General data from each of the 18 different experiments are given in train.csv and includes the experiment number, material (wax), feed rate, and clamp pressure. Outputs per experiment include tool condition (unworn and worn tools) and whether or not the tool passed visual inspection.

Time series data was collected from the 18 experiments with a sampling rate of 100 ms and are separately reported in files experiment_01.csv to experiment_18.csv. Each file has measurements from the 4 motors in the CNC (X, Y, Z axes and spindle). These CNC measurements can be used in two ways:

(1) Taking every CNC measurement as an independent observation where the operation being performed is given in the Machining_Process column. Active machining operations are labeled as "Layer 1 Up", "Layer 1 Down", "Layer 2 Up", "Layer 2 Down", "Layer 3 Up", and "Layer 3 Down".
(2) Taking each one of the 18 experiments (the entire time series) as an observation for time series classification
Note that some variables will not accurately reflect the operation of the CNC machine. This can usually be detected by when M1_CURRENT_FEEDRATE reads 50, when X1 ActualPosition reads 198, or when M1_CURRENT_PROGRAM_NUMBER does not read 0. The source of these errors has not been identified.

#### Acknowledgements about dataset
This data was extracted using the Rockwell Cloud Collector Agent Elastic software from a CNC milling machine in the System-level Manufacturing and Automation Research Testbed (SMART) at the University of Michigan.


## Prerequisites - What  do we need 
Things you need to install:

Python3.5+
FastAPIs 
Apache Airflow 
Pytests
Locusts

## Project Structure
```
Jayshil Roomie, [02.04.21 15:07]
C:.
|   Assignment 3 Requirements.pdf
|   CNC Notebook Data Science.ipynb
|   CNC_Mill_Tool_Wear.py
|   inferenceraw.py
|   inferenceraw1.py
|   inferenceraw_old.py
|   locustfile.py
|   README.md
|   test_inferenceraw.py
|
+---archive
|   |   experiment_01.csv
|   |   experiment_02.csv
|   |   experiment_03.csv
|   |   experiment_04.csv
|   |   experiment_05.csv
|   |   experiment_06.csv
|   |   experiment_07.csv
|   |   experiment_08.csv
|   |   experiment_09.csv
|   |   experiment_10.csv
|   |   experiment_11.csv
|   |   experiment_12.csv
|   |   experiment_13.csv
|   |   experiment_14.csv
|   |   experiment_15.csv
|   |   experiment_16.csv
|   |   experiment_17.csv
|   |   experiment_18.csv
|   |   README.txt
|   |   test_artifact.jpg
|   |
|   \---Train
|           train.csv
|
+---dags
|   |   CNCPipeline.py
|   |
|   \---pycache
|           CNCPipeline.cpython-38.pyc
|
\---Images
        AirflowPipeline.png
        CNC_Data_Science1.png
        CNC_Data_Science2.png
        CNC_Data_Science3.png
        Data Flow.png
        Locust1.png
        Locust2.png
        Snowflake.png

```

## Architecture:

![](https://github.com/jayshilj/Team3_CSYE7245_Spring2021/blob/main/Assignments/Assignment%3/Images/airflowarchitecture.jpg)


## Setup For Running this Project:

#### Step 1: Clone Repository
Clone this repo and edit the code with your Snowflake credentials

#### Step 2: Setup Airflow
Once your snowflake account is setup and configuration is setup, setup Airflow and start running DAGs

This is how your AIRFLOW architecture will look like: 


#### Step 3: Data Ingestion into Snowflake 

Once your DAGs run successfully your data is scrapped from Kaggle site CNC MILL,
https://www.kaggle.com/shasun/tool-wear-detection-in-cnc-mill

End result should be that all data is into Snowflake DB

![](https://github.com/jayshilj/Team3_CSYE7245_Spring2021/blob/main/Assignments/Assignment%3/Images/snowflakedb.jpg)


#### Step 4: FAST APIs  (initial authentication)

Once your DAGs run successfully your FAST APIs will be up and you can now use the FAST APIs via following link : 

http://localtest.me:8000/documentation?access_token=1234567asdfgh

Note: we have setup Dynamic token Generation for each session to enhance security


![](https://github.com/jayshilj/Team3_CSYE7245_Spring2021/blob/main/Assignments/Assignment3/Images/fastapis.jpg)


#### Step 5: Querying through APIs  

Once your FAST APIs will be up and you can now query each aspect for data in db via the FAST APIs 


Note: we have setup Dynamic token Generation for each session to enhance security


![](https://github.com/jayshilj/Team3_CSYE7245_Spring2021/blob/main/Assignments/Assignment3/Images/fastapisresult.jpg)


#### Step 6: Testing your through APIs  

Once your FAST APIs work for accessing each APIs, we will test APIs via Pytests 
and Load testing via Locusts 


![](https://github.com/jayshilj/Team3_CSYE7245_Spring2021/blob/main/Assignments/Assignment3/Images/pytests.jpg)




![](https://github.com/jayshilj/Team3_CSYE7245_Spring2021/blob/main/Assignments/Assignment3/Images/locusts.jpg)


End result should be that all tests cases designed are running 

#### Step 7: Visualizations free accessible via link




**Team Members**<br />
Akash M Dubey <br />
Jayshil Jain <br />
Sagar Shah <br/>


#### Inspiration 
YOU DONT NEED TO WORRY ABOUT DATASETS AND ALGORITHMS TO ACCESS THEM, 
WE HAVE DONE IT FOR YOU, 

YOU ARE USE OUR APIS

This APIs can be used in classification studies such as:

(1) Tool wear detection --- Supervised binary classification could be performed for identification of worn and unworn cutting tools. Eight experiments were run with an unworn tool while ten were run with a worn tool (see tool_condition column for indication).

(2) Detection of inadequate clamping --- The data could be used to detect when a workpiece is not being held in the vise with sufficient pressure to pass visual inspection (see passedvisualinspection column for indication of visual flaws). Experiments were run with pressures of 2.5, 3.0, and 4.0 bar. The data could also be used for detecting when conditions are critical enough to prevent the machining operation from completing (see machining_completed column for indication of when machining was preemptively stopped due to safety concerns).


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)