## Project
### FAST - Financial Analytics with Stock Prediction and Timeseries Forecasting

## Project Report:
https://codelabs-preview.appspot.com/?file_id=1qxniFjwkDir6NT17KkvS1zDbmIgawcrEEwbbfCtAk8k#1


## Project Proposal:
https://codelabs-preview.appspot.com/?file_id=11_uaC--B3Yz0_ux-d8Pb0SZlrfnj4xPv_C8cT1E3ZQs#1


## Web Application:
http://ec2-18-232-35-95.compute-1.amazonaws.com:8501/

## Project Structure
```
Project
C:.
|  audioapp.py
|  googletrends.py
|  jayshilapp.py
|  output.doc
|  README.md
|  stockapp-FinViz.py
|  StockScreenDemo.py
|  summary.py
|  tweetData.py
|  
+---Datasets
|      SP500.csv
|      
+---Fastwebapp
|  |  app.py
|  |  LICENSE.txt
|  |  Procfile
|  |  README.md
|  |  requirements.txt
|  |  runtime.txt
|  |  
|  +---static
|  |  |  architecture.gif
|  |  |  automobile.gif
|  |  |  bigdata.gif
|  |  |  cloud.gif
|  |  |  data.gif
|  |  |  electronics.gif
|  |  |  Final_AWS_FAST.jpg
|  |  |  forecasting.jpg
|  |  |  medical.gif
|  |  |  retail.gif
|  |  |  sentiment.gif
|  |  |  sentiment_analysis.gif
|  |  |  sentiment_analysis.png
|  |  |  stock.gif
|  |  |  stockmarket.gif
|  |  |  stock_latest.gif
|  |  |  stock_latest.jpg
|  |  |  timeforecasting.gif
|  |  |  workflow_png.png
|  |  |  
|  |  +---css
|  |  |      font-awesome.min.css
|  |  |      main.css
|  |  |      
|  |  +---css_1
|  |  |  |  font-awesome.min.css
|  |  |  |  main.css
|  |  |  |  
|  |  |  \---_notes
|  |  |          dwsync.xml
|  |  |          
|  |  +---fonts
|  |  |      fontawesome-webfont.eot
|  |  |      fontawesome-webfont.svg
|  |  |      fontawesome-webfont.ttf
|  |  |      fontawesome-webfont.woff
|  |  |      fontawesome-webfont.woff2
|  |  |      FontAwesome.otf
|  |  |      
|  |  +---fonts_1
|  |  |  |  fontawesome-webfont.eot
|  |  |  |  fontawesome-webfont.svg
|  |  |  |  fontawesome-webfont.ttf
|  |  |  |  fontawesome-webfont.woff
|  |  |  |  fontawesome-webfont.woff2
|  |  |  |  FontAwesome.otf
|  |  |  |  
|  |  |  \---_notes
|  |  |          dwsync.xml
|  |  |          
|  |  +---js
|  |  |      jquery.min.js
|  |  |      jquery.scrollex.min.js
|  |  |      main.js
|  |  |       skel.min.js
|  |  |      util.js
|  |  |      
|  |  \---js_1
|  |      |  jquery.min.js
|  |      |  jquery.scrolly.min.js
|  |      |  main.js
|  |      |  skel.min.js
|  |      |  util.js
|  |      |  
|  |      \---_notes
|  |              dwsync.xml
|  |              
|  \---templates
|          architecture.html
|          automobile.html
|          cloud.html
|          dataeda.html
|          electronics.html
|          health.html
|          index.html
|          metric.html
|          retail.html
|          sentimentanalysis.html
|          timeseriesanalysis.html
|          
+---GLUE ETL SCRIPTS
|      ETLMigrationJob
|      google_trends_automobile
|      google_trends_cloud
|      google_trends_hardware
|      google_trends_healthcare
|      google_trends_retail
|      sp500
|      TwitterStreamsETL
|      
\---Twitter
       App_Streamlit.py
       Logo1.jpg

```



## Getting Started

#### Prerequisites
1. Python3.7+
2. Docker
3. Flask
4. AWS
5. Streamlit
6. Weights and Biases
7. Twittwer Developer Account


#### Configuring the AWS CLI
You need to retrieve AWS credentials that allow your AWS CLI to access AWS resources.

1. Sign into the AWS console. This simply requires that you sign in with the email and password you used to create your account. If you already have an AWS account, be sure to log in as the root user.
2. Choose your account name in the navigation bar at the top right, and then choose My Security Credentials.
3. Expand the Access keys (access key ID and secret access key) section.
4. Press Create New Access Key.
5. Press Download Key File to download a CSV file that contains your new AccessKeyId and SecretKey. Keep this file somewhere where you can find it easily
6. Get AWS Key and create a config file
7. Setup awscli on your local machine 

#### Configuring the Twitter Developer Account
1. Go to https://developer.twitter.com/ and get key to retrive the twiiter data and paste it in a config file.
2. Request access to customer key, consumer key, secrect consumer key and secrect customer key
3. Change the Keys in the app.py file

#### Steps to get the Data
1. git clone the repo https://github.com/jayshilj/Team3_CSYE7245_Spring2021/Final Project
2. In "Data" folder we have file to run the api and the Scrapper function. This is also scheduled with AWS Lambda in AWS console to run daily and can be modified as per the need.
3. This will get us the data in S3 bucket.
4. Now, We will have a Data in S3 bucket. Now use the AWS glue scripts to build Glue jobs to extract data from S3 buckets, transform it and load it into the Redshift Data Warehouse.

#### Aws Comprehend:
1. In this repo we have python script for sentiment_analaysis we need to run that in order to get sentiment score of the scrapped data which will trigger the aws gule workflow to run the gule jobs which add the data in redshift data warehouse.

#### AWS Lambda Setup:
1. Use the Scrapper Files in the Document to setup the Lambda Function in AWS
2. The Lamabda function has to be named in the way the file is named
3. 

#### Deploying the webapp on heroku:
1. Download heroku toolbelt from  https://toolbelt.heroku.com/
2. Creating requirements.txt in which the dependencies for the package are listed on each line in the same folder as app.py. We can list the following:
Flask,
gunicorn
3. Creating runtime.txt which tells Heroku which Python version to use. We have used python-3.5.1
4. Create a Procfile. It is a text file in the root directory of the application that defines process types and explicitly declares what command should be executed to start our app. It can contain:
web: gunicorn app:app --log-file=-
5. We need to create a GitHub repository with app.py and these essential files along with.gitignore(Although it is not necessary it is recommended to include it)
6. Now our Flask app folder contains the this file structure
```
 ├── .gitignore
 ├── Procfile
 ├── app.py
 ├── requirements.txt
 │── runtime.txt
 ```
7. Go on Heroku website and after logging in click on New → Create New App.
Enter ”App name” and select the region and click on Create App and in the Deploy tab, select GitHub in Deployment method then Select the repository name and click Connect
8. Select Enable Automatic Deploys so that whenever we push changes to our GitHub it reflects on our app and Click Deploy Branch  which will deploy the current state of the branch.
If everything is successful it shows an Open App button. We can now open the app deployed on Heroku


#### Docker setup for app:
1. git clone the repo https://github.com/jayeshpatil130/CSYE7245_BDIA/tree/master/Final_Project
2. docker build -t stock_app:1.0 . -- this references the Dockerfile at . (current directory) to build our Docker image & tags the docker image with stock_app:1.0
3. Run docker images & find the image id of the newly built Docker image, OR run docker images | grep stock_app:1.0 | awk '{print $3}'
4. docker run -it --rm -p 5000:5000 {image_id} stock_app:1.0 -- this refers to the image we built to run a Docker container.

### Tests:
1. Heroku- Once App is deployed, you can spin the app from your browser, to see if its working or not.
2. Docker- You test it on 0.0.0.0:5000 or using docker-machine ip (eg : http://192.168.99.100:5000/)


## Authors
<b>[Sharvari Karnik](https://www.linkedin.com/in/sharvarikarnik25/)</b> 

<b>[Kunal Jaiswal](https://www.linkedin.com/in/kunaljaiswal4393/)</b> 

<b>[Jayesh Patil](https://www.linkedin.com/in/jayeshpatil130/)</b> 

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details