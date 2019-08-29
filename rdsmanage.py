import sys
import boto3
rds_client = boto3.client('rds',region_name="ap-south-1")

db_instance_info = rds_client.describe_db_instances()

for each_db in db_instance_info['DBInstances']:
    response = rds_client.list_tags_for_resource(ResourceName=each_db['DBInstanceArn'])
    taglist = response['TagList']
    if sys.argv[1] == each_db['DBInstanceIdentifier'] and sys.argv[2] == 'stop':
     for tag in taglist:
        if tag['Key'] == 'Name' and tag['Value'] == 'heroku' and each_db['DBInstanceStatus'] == 'available':
              db=each_db['DBInstanceIdentifier']
              status=each_db['DBInstanceStatus']
              print(db +':'+ status)
              response = rds_client.stop_db_instance(DBInstanceIdentifier=db)

    elif sys.argv[1] == each_db['DBInstanceIdentifier'] and sys.argv[2] == 'start':
     for tag in taglist:
        if tag['Key'] == 'Name' and tag['Value'] == 'heroku' and each_db['DBInstanceStatus'] == 'available':
              db=each_db['DBInstanceIdentifier']
              status=each_db['DBInstanceStatus']
              print(db +':'+ status)
              response = rds_client.start_db_instance(DBInstanceIdentifier=db)

    elif sys.argv[1] == each_db['DBInstanceIdentifier'] and sys.argv[2] == 'status':
     for tag in taglist:
        if tag['Key'] == 'Name' and tag['Value'] == 'heroku':
              db=each_db['DBInstanceIdentifier']
              status=each_db['DBInstanceStatus']
              print(db +':'+ status)

    elif sys.argv[1] == 'stop' and sys.argv[:2]:
     for tag in taglist:
        if tag['Key'] == 'Name' and tag['Value'] == 'heroku' and each_db['DBInstanceStatus'] == 'available':
              db=each_db['DBInstanceIdentifier']
              status=each_db['DBInstanceStatus']
              print(db +':'+ status)
              response = rds_client.stop_db_instance(DBInstanceIdentifier=db)

    elif sys.argv[1] == 'start' and sys.argv[:2]:
     for tag in taglist:
        if tag['Key'] == 'Name' and tag['Value'] == 'heroku' and each_db['DBInstanceStatus'] == 'stopped':
              db=each_db['DBInstanceIdentifier']
              status=each_db['DBInstanceStatus']
              print(db +':'+ status)
              response = rds_client.start_db_instance(DBInstanceIdentifier=db)

    elif sys.argv[1] == 'status' and sys.argv[:2]:
     for tag in taglist:
        if tag['Key'] == 'Name' and tag['Value'] == 'heroku':
              db=each_db['DBInstanceIdentifier']
              status=each_db['DBInstanceStatus']
              print(db +':'+ status)