import boto3
import time

elb_client = boto3.client('elb')
client = boto3.client('ec2')
ec2resource = boto3.resource('ec2')
response = elb_client.describe_instance_health(
    LoadBalancerName='testelb')

list_of_instances = []
for ec2ID in response['InstanceStates']:
    if ec2ID['State'] == "OutOfService":
        print(ec2ID['InstanceId'])
        instance = ec2resource.Instance(ec2ID['InstanceId'])
        if instance.state['Name'] != "stopped":
            elb_client.deregister_instances_from_load_balancer(
                    LoadBalancerName='testelb', Instances=[{
		            'InstanceId': '{}'.format(ec2ID['InstanceId']),
                 }]
            )
            client.stop_instances(InstanceIds=[ec2ID['InstanceId']])
        else:
            print(ec2ID['InstanceId'], "is already stopped")

		# instance = ec2resource.Instance(ec2ID['InstanceId'])
		# print(instance.state['Name'])
		# while instance.state['Name'] != "stopped":
		# 	time.sleep(5)
		# 	print("{} is stopping".format(ec2ID['InstanceId']))
		# print("{} is stopped".format(ec2ID['InstanceId']))