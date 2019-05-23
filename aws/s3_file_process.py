import boto3
import os

bucket_name = 'vaneet2019'
s3_resource = boto3.resource('s3')
my_bucket = s3_resource.Bucket(bucket_name)

s3 = boto3.client('s3')

for s3_file in my_bucket.objects.all():
	if s3_file.key.startswith('vaneet'):
		if s3_file.key.endswith('.gz'):
			if not os.path.isdir(''.join(s3_file.key.split('_')[1:3])):
				os.mkdir(''.join(s3_file.key.split('_')[1:3]))
				path = ''.join(s3_file.key.split('_')[1:3])
				my_bucket.download_file(s3_file.key, '{}/{}'.format(path, s3_file.key))
			else:
				path = ''.join(s3_file.key.split('_')[1:3])
				if not os.path.isfile(os.path.join(path, s3_file.key)):
					my_bucket.download_file(s3_file.key, '{}/{}'.format(path, s3_file.key))

