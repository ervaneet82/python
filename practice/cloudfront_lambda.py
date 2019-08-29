import boto3


def lambda_handler(event, context):
	client = boto3.client('cloudfront')
	get_cloudfront_information = client.get_distribution(Id='E3606NMHR5PPIJ')
	ETag = get_cloudfront_information['ETag']
	client.update_distribution(
		DistributionConfig={
			"CallerReference": "1540475935382",
			"Aliases": {
				"Quantity": 0
			},
			"DefaultRootObject": "",
			"Origins": {
				"Quantity": 1,
				"Items": [
					{
						"Id": "test",
						"DomainName": "suman1982.s3.amazonaws.com",
						"OriginPath": "",
						"CustomHeaders": {
							"Quantity": 0
						},
						"S3OriginConfig": {
							"OriginAccessIdentity": "origin-access-identity/cloudfront/E2IEA39FMUL7BA"
						}
					}
				]
			},
			"DefaultCacheBehavior": {
				"TargetOriginId": "test",
				"ForwardedValues": {
					"QueryString": False,
					"Cookies": {
						"Forward": "none"
					},
					"Headers": {
						"Quantity": 0
					},
					"QueryStringCacheKeys": {
						"Quantity": 0
					}
				},
				"TrustedSigners": {
					"Enabled": False,
					"Quantity": 0
				},
				"ViewerProtocolPolicy": "https-only",
				"MinTTL": 0,
				"AllowedMethods": {
					"Quantity": 2,
					"Items": [
						"HEAD",
						"GET"
					],
					"CachedMethods": {
						"Quantity": 2,
						"Items": [
							"HEAD",
							"GET"
						]
					}
				},
				"SmoothStreaming": False,
				"DefaultTTL": 86400,
				"MaxTTL": 31536000,
				"Compress": False,
				"LambdaFunctionAssociations": {
					"Quantity": 0
				},
				"FieldLevelEncryptionId": ""
			},
			"CacheBehaviors": {
				"Quantity": 0
			},
			"CustomErrorResponses": {
				"Quantity": 0
			},
			"Comment": "",
			"Logging": {
				"Enabled": False,
				"IncludeCookies": False,
				"Bucket": "",
				"Prefix": ""
			},
			"PriceClass": "PriceClass_All",
			"Enabled": True,
			"ViewerCertificate": {
				"CloudFrontDefaultCertificate": True,
				"MinimumProtocolVersion": "TLSv1",
				"CertificateSource": "cloudfront"
			},
			"Restrictions": {
				"GeoRestriction": {
					"RestrictionType": "none",
					"Quantity": 0
				}
			},
			"WebACLId": "",
			"HttpVersion": "http2",
			"IsIPV6Enabled": False

		},
		Id='E3606NMHR5PPIJ',
		IfMatch=ETag
	)