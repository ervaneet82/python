import json

with open('test.json') as f:
	route53_config_json = json.load(f)
	print(route53_config_json['resources'][0].split('/')[1])
