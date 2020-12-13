import boto3
import os
import json

ddb_client = boto3.resource('dynamodb')
table = ddb_client.Table(os.environ['tableName'])


def lambda_handler(event, context):
    """Scans all items in table"""
    sentiments = table.scan(
        ProjectionExpression="product_id, user_id, review, sentiment",
        Limit=100)

    return {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({"Sentiments": sentiments['Items']})
    }
