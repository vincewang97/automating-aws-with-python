import boto3
aws = boto3.Session(profile_name='default')
s3 = aws.resource('s3')
