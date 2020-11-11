# Sample Sentiment Analyzer
**Note: This is not Production grade and simply meant as a demo**

## Description

This project will build a serverless sentiment analyzer leveraging Amazon Comprehend's natural language processing (NLP) capabilities. The user needs to submit jobs to a queue which will trigger the rest of the workflow.

## AWS Services

* AWS Lambda
* Amazon Comprehend
* Amazon DynamoDB
* Amazon SQS

## Pre-Requisites

* SAM CLI - <https://docs.aws.amazon.com/serverless-application-model/index.html>

## Instructions

* Update deploy.sh

```bash
S3_BUCKET='my-playpen' # This bucket needs to exist in your AWS account
```

* Run deploy.sh

```bash
$ ./deploy.sh
```

## Testing
* Log on to AWS Console and browse to SQS.
* Select the sentiment-analyzer-queue
* Submit the following sample messages:

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

* Browse to DynamoDB and select the sentiments-table to see the results.


## Improvements

* Update the Lambda function to use the batch versions of the comprehend calls to lower costs and improve performance.
