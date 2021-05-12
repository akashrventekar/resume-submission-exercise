#!/bin/bash

pip3 install -U -r requirements.txt -t ./dist
cp resume_submission/*.py dist/
cd dist/
zip my-test-website.zip -r ./

aws lambda update-function-code --function-name my-test-website --zip-file fileb://my-test-website.zip --profile my-aws-account
