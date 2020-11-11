import boto3
import logging
import json
from operator import itemgetter

log = logging.getLogger()
log.setLevel(logging.DEBUG)

cmp = boto3.client('comprehend')
ddb = boto3.resource('dynamodb')
table = ddb.Table('sentiments-table')

def detect_language(review):
  response = cmp.detect_dominant_language(
    Text=review
  )
  sorted_languages = sorted(response['Languages'], key=itemgetter('Score'), reverse=True)
  log.debug(sorted_languages)
  return sorted_languages[0]['LanguageCode']

def detect_sentiment(review):
  response = cmp.detect_sentiment(
    Text=review,
    LanguageCode=detect_language(review)
  )
  log.debug(response)
  return response['Sentiment']

def lambda_handler(event, context):
  for record in event['Records']:
    body = json.loads(record['body'])
    product_id = body['product_id']
    user_id = body['user_id']
    review = body['review']
    sentiment = detect_sentiment(review)
    table.put_item(
      Item={
        'product_id': product_id,
        'user_id': user_id,
        'sentiment': sentiment,
        'review': review
      }
    )