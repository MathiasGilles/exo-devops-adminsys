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
            'Access-Control-Allow-Methods':'GET'
        }
    }

    try:
        ressource = boto3.resource('dynamodb')

        table_analyse_name = os.environ['STORAGE_DYNAMO001_NAME']
        table_analyse = ressource.Table(table_analyse_name)

        table_user_name = os.environ['STORAGE_USERS_NAME']
        table_user = ressource.Table(table_user_name)

        user_id = get_user_id(event)

        user_analyses = get_user_analyses(user_id,table_user)

        response['statusCode'] = 200
        response['body'] = get_analyses_from_id(user_analyses,table_analyse,ressource)

    except (Exception, ClientError) as error:
        print(error)
        response['statusCode'] = 400
        response['body'] = json.dumps({"error": str(error)})

    return response

def get_user_analyses(user_id, user_table):

    expression = "analyses"

    user = user_table.get_item(
        ProjectionExpression=expression,
        Key={'id':user_id}
    )

    if 'Item' not in user:
        raise ValueError('User not found')
    return user['Item']['analyses']

def get_analyses_from_id(list,item_table,ressource):

    data = ressource.batch_get_item(
        RequestItems={
            item_table.name: {
                'Keys':list,
                'ProjectionExpression':"id, title, description, created_at, transcript"
            }
        }
    )

    return json.dumps(data['Responses'][item_table.name])