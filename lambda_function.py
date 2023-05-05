import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('todoTable')
    
    http_method = event['requestContext']['http']['method']
    data = json.loads(event['body'])
    
    if http_method == "POST":
        response = table.scan()
        tabledata = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            tabledata.extend(response['Items'])
        response = tabledata
        
    elif http_method == "DELETE":
        response = table.table.delete_item(Key={
            'id':data['id']
        })
        response = response['ResponseMetadata']['HTTPStatusCode']
    elif http_method == "PUT":
        response = table.put_item(Item={'id':data['id'],'message':data['message']})
        
    
            
    return {
        'statusCode': 200,
        'body': {'event':event,
        'my_data': response}
    }
