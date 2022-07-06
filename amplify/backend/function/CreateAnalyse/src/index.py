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

      table_user_name = os.environ['STORAGE_USERS_NAME']
      table_user = ressource.Table(table_user_name)

      user_id = get_user_id(event)

      analyse_id = create_analyse(table, user_id)
      print(analyse_id)
      print(user_id)
      update_user(table_user,user_id, analyse_id)

      response['statusCode'] = 200
    except (Exception, ClientError) as error:
      response['statusCode'] = 400
      response['body'] = json.dumps({"error": str(error)})

    return response


def create_analyse(table, user_id):
    current_date = f'{str(datetime.now().isoformat())}Z'
    id = str(uuid.uuid1())

    to_create = {
        "id": id,
        "title": None,
        "description": None,
        "created_by": user_id,
        "updated_by": user_id,
        "created_at": current_date,
        "updated_at": current_date,
        "transcript": None,
    }

    table.put_item(Item=to_create)
    return id


def update_user(user_table, user_id, analyse_id):

    to_update = {
    ":al":[{'id':analyse_id}],
    }

    expression = "SET analyses = list_append(analyses, :al)"

    user_table.update_item(
        Key={'id':user_id},
        UpdateExpression=expression,
        ExpressionAttributeValues=to_update
    )