import json
import boto3
import os
from botocore.exceptions import ClientError

def handler(event, context):
    try:
      ressource = boto3.resource('dynamodb',region_name="eu-west-1")
      table_name = os.environ['STORAGE_USERS_NAME']
      table = ressource.Table(table_name)
      create_user(table, event)
    except (Exception, ClientError) as error:
        print(json.dumps({"error": str(error)}))

    return event


def create_user(table, event):
    id = event['request']['userAttributes']['sub']
    to_create = {
        "id": id,
        "analyses": []
    }


    table.put_item(Item=to_create)
