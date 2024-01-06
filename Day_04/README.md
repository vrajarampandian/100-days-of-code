Boto3 - AWS API - create or manage the  AWS resource like S3 bucket
       - Automation
	   
	   CFT - cloud Formation Templates
	   Terraform
	   
	   -> Serverless program -> lambda - cost optimitation, monitoring

codeSpace - >dev container -> Add Dev Container Configuration Files -> Modify you active configuration -> AWS CLI devcontainers

$> aws configure

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html

client = boto3.client('s3')
resource = boto3.resource('s3') # no more support

botocore - exceptions handling 
