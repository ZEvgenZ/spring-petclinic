#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-2')

#IP-address range
ip_addr = ["10.0.10.100"]
work =["db"]



# find image id ami-976152f2 / us-east-2
# Create instances
def create_instance(ip, tag):
    tag_name = {"Key": "Name", "Value": tag}
    instances = ec2.create_instances(
    ImageId='ami-2a0f324f', 
    InstanceType='t2.micro',
    KeyName='aws_ssh_key', 
    MaxCount=1,
    MinCount=1,
    NetworkInterfaces=[{'SubnetId': "subnet-6dfc4017", 
                        'DeviceIndex': 0, 
                        'AssociatePublicIpAddress': True,
                        'PrivateIpAddress': ip,
                        'Groups': ["sg-bfe75ad5",]
                        }],
    TagSpecifications=[{'ResourceType': 'instance',
                        'Tags': [tag_name]}]
        )
        
    print(instances[0].id)  
    return instances[0].wait_until_running()

for ip, tag in zip(ip_addr, work):
    create_instance(ip, tag)


for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
    print (instance.id, instance.state, instance.public_ip_address, instance.private_ip_address)
    ######hosts-file for ansible
    f_hosts=open('hosts', mode='w+')
    f_hosts.write("[hosts]\n")
    #f_hosts.write("APP_HOST ansible_ssh_host=10.0.10.200 ansible_ssh_user=ec2-user\n")
    f_hosts.write("DB_HOST ansible_ssh_host=" + instance.public_ip_address + " ansible_ssh_user=ec2-user\n")
    f_hosts.close()
