import json
import boto3
import sys
sys.path.insert(0, 'opt/messageLibrary.py')
from messageLibrary import replace_letters

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('todoTable')
    
    http_method = event['requestContext']['http']['method']
    data = json.loads(event['body'])
    
    #Gets a list of all items in the todo Table
    if http_method == "POST":
        response = table.scan()
        tabledata = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            tabledata.extend(response['Items'])
        response = tabledata
    #Deletes an item from the todo Table
    elif http_method == "DELETE":
        response = table.delete_item(Key={
            'id':data['id']
        })
    #Inserts an item into the todo Table.
    elif http_method == "PUT":
        response = table.put_item(Item={'id':data['id'],'message':replace_letters(data['message'])})
        
    return {
        'statusCode': 200,
        'body': {'event':event,
        'my_data': response}
    }
