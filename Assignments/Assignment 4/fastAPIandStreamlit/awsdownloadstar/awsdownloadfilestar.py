from boto3.session import Session
import boto3
import os
ACCESS_KEY = 'AKIA5CUSOFRV36GAHXEX'
SECRET_KEY = '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'
FILE_NAME = 'AGEN.txt'
session = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
your_bucket = s3.Bucket('wsjscrapper')
objects = your_bucket.objects.filter(Prefix='899029019755-PII-12e515b025d8d14ff824d6baae6bbe8a/output/')
for s3_file in your_bucket.objects.all():
    print(s3_file.key) # prints the contents of bucket
    # filename = s3_file.key
    # your_bucket.download_file(s3_file.key, filename)
    path, filename = os.path.split(s3_file.key)
    your_bucket.download_file(s3_file.key, filename)
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3.download_file('wsjscrapper','899029019755-PII-12e515b025d8d14ff824d6baae6bbe8a/output/','/home/akashmdubey/CSYE/Assignment4/Assignment-Trial/fastAPIandStreamlit/awsdownloadstar/')