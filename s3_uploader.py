from secrets import access_key, secret_access_key
import boto3

session = boto3.Session(region_name='eu-west-1')
s3_client = session.client ('s3', 
                       aws_access_key_id = access_key,
                       aws_secret_access_key = secret_access_key)

bucket_name = 'your bucket name'
s3_location = {'LocationConstraint': 'eu-west-1'}
s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=s3_location)
















































































