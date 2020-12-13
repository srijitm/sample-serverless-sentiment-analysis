# Sample Sentiment Analyzer
**Note: This is not Production grade and simply meant as a demo**

## Description

This project will build a serverless sentiment analyzer leveraging Amazon Comprehend's natural language processing (NLP) capabilities. 
The user needs to post a review to an endpoint (POST /sentiments), this endpoint pushes the data to a queue.
Data in the queue is processed by a lambda function, this function calls Amazon Comprehend to analyze the sentiment. Once the analysis is completed, results are save in an Amazon DynamoDB Table. 

Diagram 1


Sentiments can later be retrieved by calling GET /sentiments.

Diagram 2


## AWS Services

* AWS Lambda
* Amazon Comprehend
* Amazon DynamoDB
* Amazon SQS
* Amazon API Gateway

## Pre-Requisites

* SAM CLI - <https://docs.aws.amazon.com/serverless-application-model/index.html>

## Instructions

1. Update deploy.sh

  ```bash
  S3_BUCKET='my-playpen' # This bucket needs to exist in your AWS account
  ```

2. Run deploy.sh

  ```bash
  $ ./deploy.sh
  ```

## Testing
1. Log on to AWS Console and browse to SQS.
2. Select the sentiment-analyzer-queue and click on Send and receieve messages (button, top right)
3. Submit the following sample messages:

  *Positive*:
  ```
  {
  "product_id": "1234",
  "user_id": "user1@email.com",
  "review": "I loved this product. Did exactly what it said it will do. No complaints. Highly recommended"
  }
  ```

  *Negative*:
  ```
  {
  "product_id": "1234",
  "user_id": "user1@email.com",
  "review": "Arrived broken. Did not do boot up. Had to contact customer service who were unhelpful. Now I am out $100 and a broken device. Do not recommend."
  }
  ```

  *Mixed*:
  ```
  {
  "product_id": "1234",
  "user_id": "user2@email.com",
  "review": "Device works. Build quality is quite poor but expected for the price."
  }
  ```

4. Browse to DynamoDB and select the sentiments-table to see the results.
5. You will see that the first message (Positive) is not in the database. That is because an user can only submit one review per product. Try submitting the positive review again to see what happens.

## Improvements

* Update the Lambda function to use the batch versions of the comprehend calls to lower costs and improve performance.
* Create secondary indexes on user_id to retrieve all reviews submitted by a specific user
