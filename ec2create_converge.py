import boto3
import sys
import argparse
import subprocess
import time
import os

parser = argparse.ArgumentParser(description="To start and stop AWS services")
parser.add_argument("--action",help="Choice the action",choices=['create'])
#parser.add_argument("--region",help="Provide region where your services are located",required=True)
parser.add_argument("--build_name",help="Provide the tag name of instance ",required=True)
parser.add_argument("--build_number",help="Provide the tag number of instance ",required=True)
args = parser.parse_args()

ec2res = boto3.client('ec2', region_name="us-east-2")
# ec2 = boto3.client('ec2', region_name=args.region)
ec2 = boto3.resource('ec2', region_name="us-east-2")

def create_ec2(buildName,buildNumber):
  instances = ec2.create_instances(
    ImageId='ami-0552e3455b9bc8d50',
    InstanceType='t2.micro',
    KeyName='jenkins',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-09d0e50a129760794'
    ],
    SubnetId='subnet-0dc00c65',
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
  time.sleep(300)

def describe_instance(buildName,buildNumber):
  for instance in ec2.instances.all():
    if instance.tags is None:
      continue
    for tag in instance.tags:
      if tag['Key'] == 'Name':
        if tag['Value'] == '{}_{}'.format(buildName,buildNumber):
          print(instance.public_ip_address)
          return instance.public_ip_address


def converge_ec2(ip_address,buildName,buildNumber):
  print("IP Address :",ip_address)
  os.system('knife bootstrap {0} -i /var/lib/jenkins/workspace/jenkins.pem -x ubuntu --sudo -N {1}_{2} --node-ssl-verify-mode none'.format(ip_address,buildName,buildNumber))
  #cmd="knife bootstrap {0} -i /home/ubuntu/jenkins.pem -x ubuntu --sudo -N {1}_{2} --node-ssl-verify-mode none".format(ip_address,buildName,buildNumber)
  #print(cmd)
  #command=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  #output, err = command.communicate()
  #print(output)


if __name__ == "__main__":
  if args.action == "create":
    create_ec2(args.build_name,args.build_number)
    ip_address = describe_instance(args.build_name,args.build_number)
    converge_ec2(ip_address,args.build_name,args.build_number)
  else:
    parser.print_help()
    sys.exit(0)
