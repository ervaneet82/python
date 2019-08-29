import boto3
import datetime
from datetime import datetime, timedelta

now = datetime.now().strftime("%Y-%m-%d")
ec2 = boto3.resource('ec2', region_name="us-east-1")
my_images = ec2.images.filter(Owners=['self'])

def create_ec2_instance_image():
  for instance in ec2.instances.all():
    for tag in instance.tags:
      if 'Name' in tag['Key']:
        image=instance.create_image(
          Name="{}_{}".format(tag['Value'],now),
          InstanceId=instance.id,
          Description="Lambda created AMI of instance ",
          DryRun=False,
          NoReboot=True,
          BlockDeviceMappings=[
            {
              'DeviceName': instance.root_device_name,
              'Ebs': {
                'Encrypted': False,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2'
              },
              'NoDevice' : ''
            }
          ]
        )
        image.create_tags(
          Tags=[
            {
              'Key': 'Name',
              'Value': tag['Value']
            },
          ]
       )


def delete_images():
  for image in my_images:
    # print(image.id,image.name,image.tags)
    # for tag in image.tags:
    #   if 'Name' in tag['Key']:
    #     print(tag['Value'])
    created_at = datetime.strptime(
      image.creation_date,
      "%Y-%m-%dT%H:%M:%S.000Z",
    )
    if  datetime.now() - timedelta(7) > created_at:
      print('Deregistering {} ({})'.format(image.name, image.id))
      image.deregister()

if __name__ == "__main__":
  create_ec2_instance_image()
  delete_images()