import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('todoTable')
    
    response = table.put_item(
        Item={'id':'123','sample':'test'})
            
    return {
        'statusCode': 200,
        'body': response
    }
