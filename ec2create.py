import boto3
import sys
import argparse
import subprocess


parser = argparse.ArgumentParser(description="To start and stop AWS services")
parser.add_argument("--action",help="Choice the action",choices=['create'])
#parser.add_argument("--region",help="Provide region where your services are located",required=True)
#parser.add_argument("--build_name",help="Provide the tag name of instance ",required=True)
#parser.add_argument("--build_number",help="Provide the tag number of instance ",required=True)
args = parser.parse_args()

ec2res = boto3.client('ec2', region_name="us-east-1")
# ec2 = boto3.client('ec2', region_name=args.region)
ec2 = boto3.resource('ec2', region_name="us-east-1")

def create(buildName,buildNumber):
  instances = ec2.create_instances(
    ImageId='ami-04169656fea786776',
    InstanceType='t2.micro',
    KeyName='my_aws',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-0ae31cde537984a36'
    ],
    SubnetId='subnet-022c91928b1fd3a31',
    TagSpecifications=[
      {
        'ResourceType': 'instance',
        'Tags': [
          {
            'Key': 'Name',
            'Value': '{}_{}'.format(buildName,buildNumber)
          },
        ]
      },
    ],
  )
  instances[0].wait_until_running()
  print(instances[0].id)
  print(instances[0].public_ip_address)

def describe_instance(buildName,buildNumber):
  for instance in ec2.instances.all():
    if instance.tags is None:
      continue
    for tag in instance.tags:
      if tag['Key'] == 'Name':
        if tag['Value'] == '{}_{}'.format(buildName,buildNumber):
          return instance.public_ip_address


def converge_ec2():
  cmd = "knife client list"
  subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)


if __name__ == "__main__":
  if args.action == "create":
    #create(args.build_name,args.build_number)
    #ip_address = describe_instance(args.build_name,args.build_number)
    converge_ec2()
  else:
    parser.print_help()
    sys.exit(0)
