import boto3
import json

# ecs = boto3.client('ecs')
#
# task_definition = ecs.list_task_definitions(familyPrefix='nginx',)
#
# latest_version = task_definition['taskDefinitionArns'][-1].split('/')[1].split(':')[1]

import os
import boto3
import re
ecs = boto3.client('ecs')

response = ecs.list_clusters()

cluster_name = response['clusterArns'][0].split('/')[1]

if cluster_name == 'test1*':



# def run_task(prefix,task_name,env_name,env_value,cluster_name):
# 	task_definition = ecs.list_task_definitions(familyPrefix='{}'.format(prefix), )
# 	latest_version = task_definition['taskDefinitionArns'][-1].split('/')[1].split(':')[1]
# 	ecs.run_task(
# 		cluster=cluster_name,
# 		taskDefinition='{}:{}'.format(task_name,latest_version),
# 		overrides={
# 			"containerOverrides": [
# 				{
# 					"name": "{}".format(task_name),
# 					"environment": [
# 						{
# 							"name": "{}".format(env_name),
# 							"value": "{}".format(env_value)
# 						}
# 					]
# 				}
# 			]
# 		},
# 		count=1,
# 		startedBy='Lambda',
# 		group='bodhi-cdt-qa',
# 		launchType='EC2',
# 	)
#
# def lambda_handler(event, context):
# 	cloud_watch_event_name = event['resources'][0].split('/')[1]
# 	if cloud_watch_event_name == 'cbt':
# 		run_task(os.environ['prefix'],os.environ['task_name'],
# 			os.environ['env_name'],
# 			os.environ['env_value'])
#
