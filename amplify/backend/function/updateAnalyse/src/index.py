import json
import boto3
import os
from botocore.exceptions import ClientError
from datetime import datetime


def handler(event, context):
    response = {
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST'
        }
    }

    ressource = boto3.resource('dynamodb', region_name="eu-west-1")
    table_name = os.environ['STORAGE_DYNAMO001_NAME']
    table = ressource.Table(table_name)
    body = json.loads(event['body'])

    if body['id'] is None or len(body['id']) <= 0:
        raise ValueError('Input error: id')

    current_date = f'{str(datetime.now().isoformat())}Z'

    to_update = {
        ":title": body['title'],
        ":description": body['description'],
        ":update": current_date
    }

    expression = "SET title = :title, description = :description, updated_at= :update"

    try:
        table.update_item(
            Key={'id': body['id']},
            UpdateExpression=expression,
            ExpressionAttributeValues=to_update
        )
        response['body'] = json.dumps({'id': body['id']})
        response['statusCode'] = 200
    except (Exception, ClientError) as error:
        print(error)
        response['statusCode'] = 500
    return response
