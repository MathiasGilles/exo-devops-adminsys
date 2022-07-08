import json
import boto3
import os
from botocore.exceptions import ClientError
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
        table_user_name = os.environ['STORAGE_USERS_NAME']
        table_user = ressource.Table(table_user_name)
        table = ressource.Table(table_name)
        body = json.loads(event['body'])
        user_id = get_user_id(event)

        if body['id'] is None or len(body['id']) <= 0:
            raise ValueError('Input error: id')

        table.delete_item(
            Key={'id': body['id']}
        )

        user_analyses = update_user_analyses(user_id, table_user, body['id'])

        response['statusCode'] = 200
    except (Exception, ClientError) as error:
        print(error)
        response['statusCode'] = 400
        response['body'] = json.dumps({"error": str(error)})

    return response

def update_user_analyses(user_id, user_table, analyseId):

    expression = "analyses"

    user = user_table.get_item(
        ProjectionExpression=expression,
        Key={'id':user_id}
    )

    idx = user['Item']['analyses'].index({'id': analyseId})
    expressionAnalyse = f'REMOVE analyses[{idx}]'

    user_table.update_item(
        Key={'id': user_id},
        UpdateExpression=expressionAnalyse
    )