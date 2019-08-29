import boto3

client = boto3.client('s3')

response = client.get_bucket_notification(
    Bucket='riyanshi2016'
)

print(response['CloudFunctionConfiguration']['CloudFunction'])