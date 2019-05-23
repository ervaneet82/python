import sys
import boto3
import json

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
response = client.describe_instances()

def describe_tags(resource_id):
	output = client.describe_tags(
				Filters=[{
					'Name': 'resource-id',
					'Values': [
						"{}".format(resource_id),
					], }, ],
			)
	return output

for r in response['Reservations']:
	for i in r['Instances']:
		if i['State']['Name'] != 'terminated':
			#print("VPC Id : {}".format(i['VpcId']))
			vpc_tag_describe = describe_tags(i['VpcId'])
			for tags in vpc_tag_describe['Tags']:
				print("VPC Tags: ", tags['Key'])
			subnet_tag_describe = describe_tags(i['SubnetId'])
			print("Subnet tags: ", subnet_tag_describe)
			for sg in i['SecurityGroups']:
				print("Security Group id : {}".format(sg['GroupId']))
			for blockdevice in i['BlockDeviceMappings']:
				print("EBS Volume id: {}".format(blockdevice['Ebs']['VolumeId']))
			for interfaces in i['NetworkInterfaces']:
				print("ENI : {}".format(interfaces['Attachment']['AttachmentId']))