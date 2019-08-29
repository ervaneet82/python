import boto3
import re

ecs = boto3.client('ecs')

response = ecs.list_clusters()

for cs in response['clusterArns']:
	if re.match(r'testing-1?', cs.split('/')[1]):
		print(cs.split('/')[1])
# cluster_name = response['clusterArns'][0].split('/')[1]
#
# print(cluster_name)
#
#
# if re.match('testin*','testing'):
# 	print(cluster_name)