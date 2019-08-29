import json
import boto3
import configparser
import epoch
from datetime import date, timedelta
import sys


ssm = boto3.client('ssm')
ssm_ppath = '/staging'
lookup = ssm_ppath + '/fnms'

logs = boto3.client('logs')
response = logs.describe_log_streams(logGroupName='abc')
email = boto3.client("ses")

listOFlogStreamNames= []
message=[]
tentantID = ""
tentant_code_name = ""
    

def mail(message,tentant_code_name,tentantID,accountID):
    msg = '\n'.join(message)          
    sendEmail = email.send_email(Destination=
    {
        'ToAddresses': ['vaneet.devops@gmail.com'],
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
            'Data': 'ERROR - Global commercial staging  – {}  - {} - {}'.format(accountID,tentant_code_name,tentantID),
        },
    },
    Source='vaneet.devops@gmail.com',
    )
    

def get_config(ssm_parameter_path):
    configuration = configparser.ConfigParser()
    # Get all parameters by path
    param_details = ssm.get_parameters_by_path(
        Path=ssm_parameter_path,
        Recursive=False,
        WithDecryption=True
    )
    # Populate the ConfigParser
    if 'Parameters' in param_details and len(param_details.get('Parameters')) > 0:
        for param in param_details.get('Parameters'):
            section_name =  param.get('Name')
            config_values = json.loads(param.get('Value'))
            config_dict = {section_name: config_values}
            configuration.read_dict(config_dict)
    return configuration

def lambda_handler(event, context):
    config = get_config(ssm_ppath)
    accountID = config[lookup]['account_number']
    environment = config[lookup]['environment']
    
    for names in response['logStreams']:
        listOFlogStreamNames.append(names['logStreamName'])
        
    today_date = "2019-08-28"
    #today_date = date.today() - timedelta(days=0)
    start_time = int(epoch.parse('{}T00:00:00Z'.format(today_date)) * 1000)
    end_time = int(epoch.parse('{}T23:59:59Z'.format(today_date)) * 1000)
    
    for logname in listOFlogStreamNames:
        for log in logs.filter_log_events(logGroupName="fnmsapplicationlog",logStreamNames=[logname],startTime=start_time,endTime=end_time)['events']:
            if 'Performing import' in log['message']:
                print (log['message'])
                #tentant_code_name = log['message'].split("\'")[1]
                tentant_code_name = "hello"
                #print(tentant_code_name)
                tentantID = log['message'].split('(')[1].split(')')[0]
            if 'ERROR' in log['message']:
                message.append(log['message'])
        mail(message,tentant_code_name,tentantID,accountID)
