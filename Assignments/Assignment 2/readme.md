## ML Pipeline to train and deploy sentiment analysis model as a service
In this assignment, We have build a sentiment analysis micro service that could take a new Edgarfile in json format and generate sentiments for each statement in the referenced EDGAR file.

To build this service, we need a Sentiment analysis model that has been trained on “labeled”,“Edgar” datasets. 

Note that you need to have labeled data which means someone has to label thestatements and you need to use EDGAR datasets since we want the ML service to be optimizedfor domain-specific datasets.

In order to accomplish this, we have designed 3 pipelines. ​We have used Airflow pipelining tools to define our pipelines.

## Report

https://codelabs-preview.appspot.com/?file_id=1hUkyf5xo1fJJzFPbH9cUKZ2AtX83ExkLmnQc7rYuwZ8#0

## Prerequisites - What  do we need 
Things you need to install:
(note: if you can simply load docker file from docker hub, its containerized app)

Python3.5+\
AWS S3\
Google understanding api 
https://cloud.google.com/natural-language/docs/sentiment-tutorial \
Docker\
Postman\
Apache Airflow 


## Prerequisites - Steps
Your development and production environments are constructed by [Docker](docker.com). Install Docker for Desktop for your OS.

To verify that Docker is installed, run `docker --version`.

## Setup your Container
In this directory, we have `Dockerfile`, a blueprint for our development environment, and `requirements.txt` that lists the python dependencies.

To serve the provided pre-trained model, follow these steps:
1. `git clone` this repo
2. `cd ./assignment2`
3. `docker build -t assignment2.` -- this references the `Dockerfile` at `.` (current directory) to build our **Docker image** & tags the docker image with `akashmdubey/assignment2:latest`
4. Run `docker images` & find the image id of the newly built Docker image, OR run `docker images | grep ml_deploy_demo | awk '{print $3}'`
5. `docker run -it --rm -p 5000:5000 {image_id} /bin/bash ml/run.sh` -- this refers to the image we built to run a **Docker container**

If everything worked properly, you should now have a container running, which:

1. Spins up a Flask server that accepts POST requests at http://0.0.0.0:5000/predict

2. Runs a customized Keras sentiment classifier on the `"data"` field of the request (which should be a **list of text strings**: e.g. `'{"data": ["this is the best!", "this is the worst!"]}'`)

3. Returns a response with the model's prediction ( positive sentiment, negative sentiment)

To test this, you can either:
1. Create custom `test_api`
2. Write your own POST request (e.g. using [Postman](https://www.getpostman.com/) or `curl`), here is an example response:
```

INPUT : 
{
    "data":["hello i am good", "This is bad"]

}

OUTPUT: 
{

    "prediction": [[positive], [negative]]

}
```


## Project Structure
```
ml_deploy_demo
├── LICENSE
├── Makefile: a set of handy commands.
├── README.md
├── VERSION: a semantic version file for the codebase.
├── Dockerfile: instruction for docker image construction.
├── docker-compose.yaml: instruction for making and running multiple docker images.
├── requirements.txt: dependencies.
├── experiment_configs: a config file that defines an experiment.
│   └── default.yaml: a default exp config file.
├── experiment_output: save all training/experiment logs here.
├── log: save all non-experiment logs here (for production you would use other paths e.g. /var/log).
├── logging.yaml: a config path for logging.
├── ml_deploy_demo
│   ├── api: the Flask app for running an ML API service.
│   │   ├── app.py
│   │   └── ml_app.py
│   ├── models: ML model/algo definitions go here.
│   │   └── neural_networks.py
│   ├── pipelines: training pipelines (for demo purpose).
│   │   └── sklearn.py
│   │   └── keras.py
│   ├── preprocessing: feature engineering, data augmentation/transformations.
│   │   └── preprocessing.py
│   ├── run.py: an entry module for Flask
│   ├── run.sh: an entry script for Flask
│   ├── train.py: the module for training.
│   ├── predict.py: the module for predicting.
│   └── util: utility functions.
│       └── utils.py
├── models: a local model registry. Models that are acceptably good are promoted to move here.
│   └── iris: a task name.
│       └── v1.joblib: a model with its version.
├── notebooks: notebook files are here.
├── scripts: utility commands go here (also things that could be run by docker runtime).
│   └── start_docker.sh
│   └── stop_docker.sh
├── setup.py: an instruction for packaging the codebase as a python package.
└── tests
```

## Setup For Running this Project:

#### Step 0: Clone Project, Setup Airflow
Clone this repo and edit the code with your AWS Credentials, Google Credentials and your s3 bucket path and then setup the Apache Airflow

#### Step 1 : Part 1 Annotation Pipeline
Run the annotation pipeline in Apache Airflow, you will have the processed files & label files using Google APIs saved in your bucket.

#### Step 2 : Part 2 Training Pipeline
Run the training pipeline in Apache Airflow, you will have the h5 model saved in your bucket.

#### Step 3 : Part 3: Microservices
Build a Docker Image, create a Docker Container and run the container. If everything is working properly, you should be able to send HTTP POST requests to http://localhost:5000/predict and get results back from the model!

#### Step 4 : Part 4: Inference Pipeline
Once  everything is working properly, We will use Inference APIs to call flat files and do preprocessing on files and sent it against built http://localhost:5000/predict and get results back from the model !


You can test this using Postman.

## Authors 
<b>[Akash M Dubey](https://www.linkedin.com/in/akashmdubey/)</b> 

<b>[Jayshil Jain](https://www.linkedin.com/in/)</b> 

<b>[Sagar Shah](https://www.linkedin.com/in/)</b> 
