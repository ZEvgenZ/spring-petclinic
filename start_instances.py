#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-2')

# create VPC
#session = boto3.session.Session()
#ec2_client = session.client('ec2', region_name='us-east-2')
#c2_resource = session.resource('ec2', region_name='us-east-2')
#create_vpc_response = ec2_client.create_vpc(CidrBlock='10.0.0.0/16')
#vpc = ec2_resource.Vpc(create_vpc_response["Vpc"]["VpcId"])


#vpc = ec2.create_vpc(CidrBlock='192.168.111.0/16')

# we can assign a name to vpc, or any resource, by using tag
#vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc_1000"}])
#vpc.wait_until_available()
#print(vpc.id)

# create then attach internet gateway
#create_ig_response = ec2_client.create_internet_gateway()
#ig_id = create_ig_response["InternetGateway"]["InternetGatewayId"]
#ig_id = igw-a812fac1
#ig = ec2.create_internet_gateway()
#vpc.attach_internet_gateway(InternetGatewayId=ig_id)
#print(ig_id)

# create a route table and a public route
#for route_table in vpc.route_tables.all():  # There should only be one route table to start with
#    route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=ig_id
#)
#print(route_table.id)

# create subnet
#subnet = vpc.create_subnet(CidrBlock='10.0.0.0/24', AvailabilityZone="{}{}".format('us-east-2', 'a'))
#print(subnet.id)
#subnet = 'subnet-fa255292'

# associate the route table with the subnet
#route_table.associate_with_subnet(SubnetId=subnet.id)

# Create sec group
#sec_group = ec2.create_security_group(
#    GroupName='sg_web', Description='sg_web sec group', VpcId=vpc.id)
#sec_group.authorize_ingress(
#    CidrIp='0.0.0.0/0',
#    IpProtocol='icmp',
##    FromPort=-1,
#    ToPort=-1
#)
#sec_group.authorize_ingress(
#    CidrIp='0.0.0.0/0',
#    IpProtocol='tcp',
#    FromPort=80,
#    ToPort=80
#)
#sec_group.authorize_ingress(
#    CidrIp='0.0.0.0/0',
#    IpProtocol='tcp',
#    FromPort=22,
#    ToPort=22
#)
#sec_group.authorize_ingress(
#    CidrIp='0.0.0.0/0',
#    IpProtocol='tcp',
#    FromPort=443,
#    ToPort=443
#)
#sec_group.authorize_ingress(
#    CidrIp='0.0.0.0/0',
#    IpProtocol='tcp',
#    FromPort=3306,
#    ToPort=3306
#)
#print(sec_group.id)

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
    NetworkInterfaces=[{'SubnetId': "subnet-fa255292", 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': ["sg-c4d22aae",]}]
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
    NetworkInterfaces=[{'SubnetId': "subnet-fa255292", 'DeviceIndex': 0, 'AssociatePublicIpAddress': False, 'Groups': ["sg-c4d22aae",]}]
)
instances[0].wait_until_running()
print(instances[0].id)

for instance in ec2.instances.all():
    print (instance.id, instance.state)
