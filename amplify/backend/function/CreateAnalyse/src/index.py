import json
import boto3
import os
import uuid
from botocore.exceptions import ClientError
from datetime import datetime
from utils import get_user_id

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
      create_analyse(table, event)
      response['statusCode'] = 200
    except (Exception, ClientError) as error:
      response['statusCode'] = 400
      response['body'] = json.dumps({"error": str(error)})

    return response


def create_analyse(table, event):
    current_date = f'{str(datetime.now().isoformat())}Z'
    id = str(uuid.uuid1())
    userId = get_user_id(event)

    to_create = {
        "id": id,
        "title": None,
        "description": None,
        "created_by": userId,
        "updated_by": userId,
        "created_at": current_date,
        "updated_at": current_date,
        "transcript": None,
    }

    table.put_item(Item=to_create)
