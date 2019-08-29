import boto3
from termcolor import colored
import argparse

class Ec2Information:
  def __init__(self):
    """Initialize the ec2 resource connection using boto3"""
    self.ec2conn = boto3.resource('ec2', region_name="us-east-1")

  def get_ec2_information(self):
    """
      This function will return the ec2 instance properties in json format.
    """
    for i in self.ec2conn.instances.all():

      print("Id: {0}\tState: {1}\tLaunched: {2}\tRoot Device Name: {3}".format(
        colored(i.id, 'cyan'),
        colored(i.state['Name'], 'green'),
        colored(i.launch_time, 'cyan'),
        colored(i.root_device_name, 'cyan')
      ))

      print("\tArch: {0}\tHypervisor: {1}".format(
        colored(i.architecture, 'cyan'),
        colored(i.hypervisor, 'cyan')
      ))

      print("\tPriv. IP: {0}\tPub. IP: {1}".format(
        colored(i.private_ip_address, 'red'),
        colored(i.public_ip_address, 'green')
      ))

      print("\tPriv. DNS: {0}\tPub. DNS: {1}".format(
        colored(i.private_dns_name, 'red'),
        colored(i.public_dns_name, 'green')
      ))

      print("\tSubnet: {0}\tSubnet Id: {1}".format(
        colored(i.subnet, 'cyan'),
        colored(i.subnet_id, 'cyan')
      ))

      print("\tKernel: {0}\tInstance Type: {1}".format(
        colored(i.kernel_id, 'cyan'),
        colored(i.instance_type, 'cyan')
      ))

      print("\tRAM Disk Id: {0}\tAMI Id: {1}\tPlatform: {2}\t EBS Optimized: {3}".format(
        colored(i.ramdisk_id, 'cyan'),
        colored(i.image_id, 'cyan'),
        colored(i.platform, 'cyan'),
        colored(i.ebs_optimized, 'cyan')
      ))

      print("\tBlock Device Mappings:")
      for idx, dev in enumerate(i.block_device_mappings, start=1):
        print("\t- [{0}] Device Name: {1}\tVol Id: {2}\tStatus: {3}\tDeleteOnTermination: {4}\tAttachTime: {5}".format(
          idx,
          colored(dev['DeviceName'], 'cyan'),
          colored(dev['Ebs']['VolumeId'], 'cyan'),
          colored(dev['Ebs']['Status'], 'green'),
          colored(dev['Ebs']['DeleteOnTermination'], 'cyan'),
          colored(dev['Ebs']['AttachTime'], 'cyan')
        ))

      print("\tTags:")
      for idx, tag in enumerate(i.tags, start=1):
        print("\t- [{0}] Key: {1}\tValue: {2}".format(
          idx,
          colored(tag['Key'], 'cyan'),
          colored(tag['Value'], 'cyan')
        ))

      print("\tProduct codes:")
      for idx, details in enumerate(i.product_codes, start=1):
        print("\t- [{0}] Id: {1}\tType: {2}".format(
          idx,
          colored(details['ProductCodeId'], 'cyan'),
          colored(details['ProductCodeType'], 'cyan')
        ))

      print("Console Output:")
      # Commented out because this creates a lot of clutter..
      # print(i.console_output()['Output'])

      print("--------------------")

  def startec2Instance(self):
    """Starting the instance..."""
    self.ec2conn.start_instances(instance_ids="i-12345678")

  def stopec2Instance(self):
    ec2.stop_instances(instance_ids="i-12345678")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="To start and stop AWS services")
  parser.add_argument("--action",help="Choice the action",choices=['start','stop'],required=True)
  parser.add_argument("--region",help="Provide region where your services are located",choices=[])
  ec2obj = Ec2Information()
  ec2obj.get_ec2_information()
