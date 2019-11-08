import boto3
from wand.image import Image
import json


s3 = boto3.client('s3')


def lambda_handler(event, context):
    bucketname=(event["Records"][0]["s3"]["bucket"]["name"])
    key= (event["Records"][0]["s3"]["object"]["key"])
    print(event["Records"][0]["s3"]["bucket"]["name"])
    with open('/tmp/image.jpg', 'wb') as data:
        s3.download_fileobj(bucketname, key, data)

    with Image(filename='/tmp/image.jpg') as img:
        print('width =', img.width)
        print('height =', img.height)
        img.resize(200, 200)

        #this will save the resized file
        img.save(filename='/tmp/image.jpg')

    resizeName=key
    upload = boto3.resource('s3')
    print("executing ....")
    s3.upload_file('/tmp/' + image.jpg, bucketname, 'screeners/images/mobile/{}'.format(resizeName))
    #upload.Object(bucketname/screeners/images/mobile/, resizeName).upload_file('/tmp/image.jpg')
    print("Done....")
