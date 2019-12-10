import json
import boto3
import epoch
from datetime import date, timedelta
import sys

LOG_NAME = 'fnmsapplicationlogstaging'
ENV = LOG_NAME.split("fnmsapplicationlog")[1]
GLOBAL_COMMERCIAL = "Global commercial"
US_SECURE = "US Secure"
AU_DOMESTIC = "AU Domestic"


logs = boto3.client('logs')
response = logs.describe_log_streams(logGroupName=LOG_NAME)
email = boto3.client("ses")

listOFlogStreamNames= []
message=[]
tentantID = ""
tentant_code_name = ""


def mail(message, tentant_code_name, tentant_id , account_id):

    if account_id == "302847890227":
	    friendly_name = "Global Commercial"
        msg = '\n'.join(message)
        sendEmail = email.send_email(Destination=
        {
            'ToAddresses': ['ameeth.reddy@dxc.com'],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': '{}'.format(msg),
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'ERROR - {} {} – ({})  - {} - ({})'.format(friendly_name, ENV, account_id,tentant_code_name,tentant_id),
            },
        },
        Source='ameeth.reddy@dxc.com',
        )
    elif account_id == "516513809217":
        msg = '\n'.join(message)
        friendly_name = "US Secure"
        sendEmail = email.send_email(Destination=
        {
            'ToAddresses': ['ameeth.reddy@dxc.com'],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': '{}'.format(msg),
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'ERROR - {} {} – ({})  - {} - ({})'.format(friendly_name, ENV, account_id,tentant_code_name,tentant_id),
            },
        },
        Source='ameeth.reddy@dxc.com',
        )
    elif account_id == "996641956517":
		friendly_name = "AU Domestic"
        msg = '\n'.join(message)
        sendEmail = email.send_email(Destination=
        {
            'ToAddresses': ['ameeth.reddy@dxc.com'],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': '{}'.format(msg),
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'ERROR - {} {} – ({})  - {} - ({})'.format(friendly_name, ENV, account_id,tentant_code_name,tentant_id),
            },
        },
        Source='ameeth.reddy@dxc.com',
        )


def lambda_handler(event, context):
    tentantID = ""
    tentant_code_name =""
    accountID= context.invoked_function_arn.split(':')[4]

    for names in response['logStreams']:
        listOFlogStreamNames.append(names['logStreamName'])

    today_date = "2019-09-10"
    #today_date = date.today() - timedelta(hour=1)
    start_time = int(datetime.now().timestamp())
    end_time = int((datetime.now() - timedelta(hours=1)).timestamp())

    for logname in listOFlogStreamNames:
        message = []
        for log in logs.filter_log_events(logGroupName=LOG_NAME, logStreamNames=[logname],startTime=start_time,endTime=end_time)['events']:
            if 'Performing import' in log['message']:
                tentant_code_name = log['message'].split("\'")[1]
                tentantID = log['message'].split('(')[1].split(')')[0]

            if 'ERROR' in log['message']:
                message.append(log['message'])

        if not (tentant_code_name and tentantID):
            print("No Log")
        elif message:
            mail(message,tentant_code_name,tentantID,accountID)
        else:
          pass