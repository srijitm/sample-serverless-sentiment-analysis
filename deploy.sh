#! /bin/bash

S3_BUCKET='gmansilla-sentiment'
STACK_NAME='sentiment-analyzer'

sam build
sam deploy sam deploy --stack-name ${STACK_NAME} --s3-bucket ${S3_BUCKET} --capabilities CAPABILITY_NAMED_IAM