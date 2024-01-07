AWS Lambda
AWS Lambda is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. 
It is designed to enable developers to run code without provisioning or managing servers.
It executes code in response to events and automatically manages the computing resources required by that code

Advanced settings - Enable function URLInfo
Use function URLs to assign HTTP(S) endpoints to your Lambda function.

The Lambda function handler is the method in your function code that processes events

import json
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }