import boto3
import time
import epoch
import sys
from datetime import date, timedelta


client = boto3.client('logs')
stream_batch = client.describe_log_streams(logGroupName='/aws/lambda/slack',
                                           orderBy='LastEventTime',
                                           descending=True)
logName = stream_batch['logStreams'][0]['logStreamName']

start = stream_batch['logStreams'][0]['firstEventTimestamp']
end = stream_batch['logStreams'][0]['lastEventTimestamp']


response = client.get_log_events(logGroupName='/aws/lambda/slack',
                                 logStreamName=logName)

print(response)
if not 'ERROR' in response:
	print('Success')
else:
	print('Failure')

start_time = time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(start/1000.))
end_time = time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(end/1000.))

