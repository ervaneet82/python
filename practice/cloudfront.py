import boto3

client = boto3.client('cloudfront')

get = client.get_distribution(Id='E3606NMHR5PPIJ')

if get['Distribution']['DistributionConfig']['Origins']['Items'][0]['DomainName'] == "riyanshi2018.s3.amazonaws.com"

