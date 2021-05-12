# resume-submission-exercise
This repo contains code that will be used for resume submission exercise

## Features
This code is deployed on AWS Lambda which provides answers to specific questions

## Tests
Tests are written in pytest and are in the tests folder. This is the documentation for what the code does.

## Design

I have used API Gateway backed by Lambda (Integration request: Lambda proxy as that is easier for plain text replies)

My initial thought process for the puzzle:
Few ways that would help solve problem:
Fill in the blanks approach
Use BST

Please refer to the tests on conversion of the input to output

Time Complexity: O(n^2)
Space Complexity: O(n^2)


## CI

The ci folder has a shell script to upload the zip file with one command `sh lambda_update.sh`. You will have to update the credentials file with your aws credentials
