import boto3
import json

with open('route53.json') as f:
	route53_config_json = json.load(f)
	client = boto3.client('route53')
	route53.change_resource_record_sets(
		HostedZoneId='Z2EHBWZL1IOKJR',
		ChangeBatch=route53_config_json
	)