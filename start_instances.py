#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-2')

#IP-address range
ip_addr = ["10.0.10.100", "10.0.10.200"]

#hosts-file for ansible
f_hosts=open('hosts', mode='w+')
f_hosts.write("[hosts]\n")
f_hosts.write("APP_VM ansible_ssh_host=10.0.10.200 ansible_ssh_user=ec2-user\n")
f_hosts.write("DB_VM ansible_ssh_host=10.0.10.100 ansible_ssh_user=ec2-user\n")
f_hosts.close()


# find image id ami-976152f2 / us-east-2
# Create instances
def create_instance(ip):
    instances = ec2.create_instances(
    ImageId='ami-2a0f324f', 
    InstanceType='t2.micro',
    KeyName='aws_pair_keys', 
    MaxCount=1,
    MinCount=1,
    NetworkInterfaces=[{'SubnetId': "subnet-6dfc4017", 
                        'DeviceIndex': 0, 
                        'AssociatePublicIpAddress': True,
                        'PrivateIpAddress': ip,
                        'Groups': ["sg-bfe75ad5",]
                        }],
        )
    print(instances[0].id)  
    return instances[0].wait_until_running()


for ip in ip_addr:
    create_instance(ip)


for instance in ec2.instances.all():
    print (instance.id, instance.state)
