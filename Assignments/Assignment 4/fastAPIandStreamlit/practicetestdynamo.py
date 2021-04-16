import boto3  # import Boto3
import json


ACCESS_KEY_ID = 'AKIA5CUSOFRV36GAHXEX'
ACCESS_SECRET_KEY = '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'

# dynamodb = boto3.resource('dynamodb',region_name='REGION', ) 
dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=ACCESS_KEY_ID,
                    aws_secret_access_key=ACCESS_SECRET_KEY,
                    region_name='us-east-1')


table = dynamodb.Table('users')

response = table.scan()

OTP = response['Items']


# dynamodbc = boto3.resource('dynamodb',
#                     aws_access_key_id=ACCESS_KEY_ID,
#                     aws_secret_access_key=ACCESS_SECRET_KEY,
#                     region_name='us-east-1')

dynamoTable = dynamodb.Table('users')


# Code to Put the Item

# dynamoTable.put_item(
#     Item={
#         'login':'michaeljordan'
#     }
# )

 

if __name__ == '__main__':
    # device_table = create_devices_table()
    # Print tablle status
    i = 0
    while i < len(OTP):
        #print(OTP[i])
        x = OTP[i]['login']
        print(x)
        i=i+1
    
    #print(OTP)
