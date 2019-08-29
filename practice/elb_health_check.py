import json

with open('result.json') as f:
	updateconfig = json.load(f)
	print(updateconfig[0]['Sns']['Message']['Trigger']['Threshold'])