import json
from pprint import pprint
import re

events='{Records": [{"EventSource": "aws:sns","EventVersion": "1.0","EventSubscriptionArn": "arn:aws:sns:us-east-1:610014150274:route53-cloudfront-healthcheck-bodhi:3ea0bc4e-54b1-4a63-a4ca-8ec1f2316be4","Sns": {"Type": "Notification","MessageId": "92a50a84-9793-51dd-b2bc-5ed0c0689d9c","TopicArn": "arn:aws:sns:us-east-1:610014150274:route53-cloudfront-healthcheck-bodhi","Subject": "None","Message": "east"}}]}'

data = json.loads(events)
print(data['Records'][0]['Sns']['Message'])



# with open('/tmp/lambda.json') as f:
#     data = json.load(f)
#
# print(data['Records'][0]['Sns']['Message'])