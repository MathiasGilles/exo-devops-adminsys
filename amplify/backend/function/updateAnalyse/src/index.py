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

    path_param = event['pathParameters']
    analyse_id = path_param['proxy']

    if analyse_id is None or len(analyse_id) <= 0:
        raise ValueError('Input error: analyse_id')

    current_date = f'{str(datetime.now().isoformat())}Z'

    to_update = {
        ":title": event['body']['title'],
        ":description": event['body']['description'],
        ":update": current_date
    }

    expression = "SET title = :title, description = :description, updated_at= :update"

    try:
        table.update_item(
            Key={'id': analyse_id},
            UpdateExpression=expression,
            ExpressionAttributeValues=to_update
        )
        response['body'] = json.dumps({'analyse_id': analyse_id})
    except (Exception, ClientError) as error:
        print(error)

    return response
