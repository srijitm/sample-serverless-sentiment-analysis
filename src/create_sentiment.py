import boto3
import os
import json

sqs_client = boto3.client('sqs')
queue_name = os.environ['queueName']


def lambda_handler(event, context):
    """Main Handler: gets event data and pushes it to SQS"""
    try:
        body = json.loads(json.dumps(event['body']))
        result = sqs_client.send_message(QueueUrl=queue_name, MessageBody=body)
        if result.get('Failed'):
            raise Exception("Message could not be sent to SQS")

        return {
            "statusCode": 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"Success": True})
        }

    except Exception as err:
        print("Error: ", err)
        raise err
