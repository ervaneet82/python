import boto3
import sys
import argparse


parser = argparse.ArgumentParser(description="To start and stop AWS services")
parser.add_argument("--action",help="Choice the action",choices=['start','stop','terminate'])
parser.add_argument("--region",help="Provide region where your services are located",required=True)
parser.add_argument("--tag",help="Provide the tag",required=True)
args = parser.parse_args()

ec2 = boto3.client('ec2', region_name=args.region)
# ec2 = boto3.client('ec2', region_name=args.region)
ec2res = boto3.resource('ec2', region_name=args.region)


def stop(ec2tag):
  for instance in ec2res.instances.all():
    for tag in instance.tags:
      if ec2tag in tag['Value']:
        print("Stopping instance : " ,instance.id)
        #ec2.stop_instances(InstanceIds='i-095ea4297f0e30ea2')
        response = ec2.stop_instances(
          InstanceIds=[
            instance.id,
          ],
          DryRun=False,
          Force=True
        )
        print(response['InstanceId'])
def start(ec2tag):
  for instance in ec2res.instances.all():
    for tag in instance.tags:
      if ec2tag in tag['Value']:
        print("Starting instance : " ,instance.id)
        response = ec2.start_instances(
          InstanceIds=[
            '{}'.format(instance.id),
          ]
        )
        print(response['StartingInstances'][0]['CurrentState']['Name'])

def terminate(ec2tag):
  for instance in ec2res.instances.all():
    for tag in instance.tags:
      if ec2tag in tag['Value']:
        print("Terminating instance : " ,instance.id)
        response = ec2.terminate_instances(
          InstanceIds=[
            '{}'.format(instance.id),
          ]
        )
        print(response['TerminatingInstances'][0]['CurrentState']['Name'])
if __name__ == "__main__":
  if args.action == "start":
    start(args.tag)
  elif args.action == "stop":
    stop(args.tag)
  elif args.action == "terminate":
    terminate(args.tag)
  else:
    parser.print_help()
    sys.exit(0)