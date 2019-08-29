import boto3


client = boto3.client('autoscaling')

set_desired_capacity = client.set_desired_capacity(
    AutoScalingGroupName='mygroup',
    DesiredCapacity=1
)



