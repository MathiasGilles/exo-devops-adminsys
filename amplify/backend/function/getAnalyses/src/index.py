import json
import boto3
import os
from botocore.exceptions import ClientError
#from utils import get_user_id
def handler(event, context):
    try:
        ressource = boto3.resource('dynamodb',region_name="eu-west-1")

        table_analyse_name = os.environ['STORAGE_DYNAMO001_NAME']
        table_analyse = ressource.Table(table_analyse_name)

        table_user_name = os.environ['STORAGE_USERS_NAME']
        table_user = ressource.Table(table_user_name)

        #user_id = get_user_id(event)
        user_id = "099575db-7744-4c70-90fd-2a73da0fc285"

        user_analyses = get_user_analyses(user_id,table_user)

        analyses = get_analyses_from_id(user_analyses,table_analyse,ressource)

    except (Exception, ClientError) as error:
        analyses = json.dumps({"error": str(error)})

    return analyses

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

    return data['Responses'][item_table.name]