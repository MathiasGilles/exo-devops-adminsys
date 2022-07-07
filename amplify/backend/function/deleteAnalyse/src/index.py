import json
import boto3
import os

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

      analyse_id = delete_analyse(table, user_id)

      response['body']=json.dumps({'analyse_id': analyse_id})
      response['statusCode'] = 200
    except (Exception, ClientError) as error:
      print(error)
      response['statusCode'] = 400
      response['body'] = json.dumps({"error": str(error)})

    return response

def delete_analyse(table, user_id):
    id = str(uuid.uuid1())

    to_delete = {
        "id": id
    }

    table.delete_item(Item=to_delete)
    return id

