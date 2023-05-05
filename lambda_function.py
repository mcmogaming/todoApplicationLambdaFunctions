import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('todoTable')
    
    http_method = event['requestContext']['http']['method']
    
    #Add an item to db
    
    #Delete an item from db
    
    #List all items from db
    
    
    response = table.put_item(
        Item={'id':'123','sample':'test'})
            
    return {
        'statusCode': 200,
        'body': event,
        'method': http_method
    }
