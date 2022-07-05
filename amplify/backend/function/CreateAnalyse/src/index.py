import json
import boto3
import os
import uuid
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
    try:
      ressource = boto3.resource('dynamodb',region_name="eu-west-1")
      table_name = os.environ['STORAGE_DYNAMO001_NAME']
      table = ressource.Table(table_name)
      #create_analyse(table,event['body'])
      create_analyse(table)
      response['statusCode'] = 200
    except (Exception, ClientError) as error:
      response['statusCode'] = 400
      response['body'] = json.dumps({"error": str(error)})

    return response


def create_analyse(table,body):
    current_date = f'{str(datetime.now().isoformat())}Z'
    id = str(uuid.uuid1())

    to_create = {
        "id": id,
        "title": body['title'],
        "description": body['description'],
        "created_by": None,
        "updated_by": None,
        "created_at": current_date,
        "updated_at": current_date,
        "transcript": None,
    }

    table.put_item(Item=to_create)
