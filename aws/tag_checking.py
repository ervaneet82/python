import sys
import boto3
import json
import re

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
response = client.describe_instances()
# print(response)
# sys.exit()
def describe_tags(resource_id):
	search_tags = client.describe_tags(
				Filters=[{
					'Name': 'resource-id',
					'Values': [
						"{}".format(resource_id),
					], }, ],
			)

	for tags in search_tags['Tags']:
		if 'BillingID' not in tags['Key']:
			create_tag(resource_id)

	return search_tags


def create_tag(resource_id):
	client.create_tags(
		Resources=[
			'{}'.format(resource_id)
		],
		Tags=[
			{
				'Key': 'BillingID',
				'Value': 'FDB',
			},
		],
	)

for r in response['Reservations']:
	for i in r['Instances']:
		if i['State']['Name'] != 'terminated':
			describe_tags(i['InstanceId'])
			describe_tags(i['VpcId'])
			describe_tags(i['SubnetId'])
			describe_sg_tags(i['SecurityGroups'])
			for sg in i['SecurityGroups']:
				describe_tags(sg['GroupId'])
				#print("Security Group id : {}".format(sg['GroupId']))
			# #for blockdevice in i['BlockDeviceMappings']:
			# 	print("EBS Volume id: {}".format(blockdevice['Ebs']['VolumeId']))
			# for interfaces in i['NetworkInterfaces']:
			# 	print("ENI : {}".format(interfaces['Attachment']['AttachmentId']))