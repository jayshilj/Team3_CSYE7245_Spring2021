#### Lab 1 - AWS Basics

1. Google Docs Link : https://docs.google.com/document/d/1ZC_bfu3FDKI9gngLEwzm7J9j7NsGaTpQNSK3bS-WRt0/edit#

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1ZC_bfu3FDKI9gngLEwzm7J9j7NsGaTpQNSK3bS-WRt0#0

### Getting Started with AWS

#### Requirements

```
pip3 install Faker
pip3 install boto3
```

#### Contents

- `s3_upload.py` - Python script to generate some fake data using Faker and upload to your S3 Bucket 
- `s3_download.py` - Download the file of your choice from S3 to your local environemnt 
- `comprehend_demo.py` - Use AWS Comprehend to detect sentiment and extract PII features from your data. Additonal APIs can be found [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html)
- Lambda Functions - Deploying Lambda functions using Python Lambda. Documentation and boilerplate code is available on [this repository](https://github.com/holladileep/lambda-serverless-py) 
