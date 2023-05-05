import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('todoTable')
    
    http_method = event['requestContext']['http']['method']
    data = json.loads(event['body'])
    
    if http_method == "GET":
        response = table.scan()
        response = response['Items']
    elif http_method == "DELETE":
        response = table.table.delete_item(Key={
            'id':data['id']
        })
    elif http_method == "PUT":
        response = table.put_item(Item={'id':data['id'],'message':data['message']})
        
    
            
    return {
        'statusCode': 200,
        'body': {'event':event,
        'my_data': response}
    }
