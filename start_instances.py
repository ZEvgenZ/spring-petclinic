#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-2')

# find image id ami-976152f2 / us-east-2
# Create instances
instances = ec2.create_instances(
    ImageId='ami-976152f2', 
    InstanceType='t2.micro',
    KeyName='aws_pair_keys', 
    MaxCount=1,
    MinCount=1,
    #SubnetId = "subnet-fa255292",
    #SecurityGroupIds = ["sg-c4d22aae"],
    #AssociatePublicIpAddress = True
    #Tags=[{'Key': 'Name', 'Value': 'db_host'}],
    NetworkInterfaces=[{'SubnetId': "subnet-fa255292", 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'PrivateIpAddress': '10.0.10.200', 'Groups': ["sg-c4d22aae",]}],
    #TagSpecifications = [
    #        {
    #            
    #            'Tags': [
    #                {
    #                    'Key': 'Name',
    #                    'Value': "db_host"
    #                },
    #            ]
    #        },
    #    ]
)   
instances[0].wait_until_running()
instances = ec2.create_instances(
    ImageId='ami-976152f2', 
    InstanceType='t2.micro',
    KeyName='aws_pair_keys', 
    MaxCount=1,
    MinCount=1,
    #SubnetId = "subnet-fa255292",
    #SecurityGroupIds = ["sg-c4d22aae"],
    #AssociatePublicIpAddress = False
    #Tags=[{'Key': 'Name', 'Value': 'app_host'}],
    NetworkInterfaces=[{'SubnetId': "subnet-fa255292", 'DeviceIndex': 0, 'AssociatePublicIpAddress': False, 'PrivateIpAddress': '10.0.10.100', 'Groups': ["sg-c4d22aae",]}],
    #TagSpecifications = [
    #        {
    #            
    #            'Tags': [
    #                {
    #                    'Key': 'Name',
    #                    'Value': "app_host"
    #                },
    #            ]
    #        },
    #    ]
)
instances[0].wait_until_running()
print(instances[0].id)

for instance in ec2.instances.all():
    print (instance.id, instance.state)

f_hosts=open('hosts', mode='w+')
f_hosts.write("[hosts]")
f_hosts.write("APP_VM ansible_ssh_host=10.0.10.100 ansible_ssh_user=ec2-user")
f_hosts.write("DB_VM ansible_ssh_host=10.0.10.200 ansible_ssh_user=ec2-user")
f_hosts.close()

#f_hosts=open('/etc/ansible/hosts', mode='a')