import json
import boto3
import os

def handler(event, context):
  print('received event:')
  print('boto')
  print(boto3.__version__)
  print(event)
  ressource = boto3.resource('dynamodb',region_name="eu-west-1")
  table_name = os.environ['STORAGE_DYNAMO001_NAME']
  table = ressource.Table(table_name)
  to_update = {
      ":title": event,
  }

  expression = "SET title = list_append(analyses, :title)"
  user_table.update_item(
      Key={'id':user_id},
      UpdateExpression=expression,
      ExpressionAttributeValues=to_update
  )