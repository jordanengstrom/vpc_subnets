"""
1st-Iteration Exercise:
Create an executable script that will use the AWS CLI to print the CIDR blocks of the VPC and of all subnets
in it.
"""

import boto3


def get_vpc_from_user():
    print('Please supply a VPC ID: ')
    vpc_id = input()
    print("Using VPC ID:", vpc_id)
    return vpc_id


def get_vpc_cidr(_vpc_id: str):
    # Declare ec2 resource
    ec2 = boto3.resource('ec2')

    # Get VPC resource using Ec2 resource by supplying VPC ID
    vpc = ec2.Vpc(_vpc_id)
    print("VPC CIDR:", vpc.cidr_block)
    return vpc.cidr_block, vpc


def main():
    # Get CIDR blocks => (CIDR = Classless Inter-Domain Routing)
    vpc_id = get_vpc_from_user()
    cidr_block, vpc = get_vpc_cidr(vpc_id)

    # Check whether VPC has subnets and display them accordingly
    subnets = list(vpc.subnets.all())
    if len(subnets) > 0:
        print("\nSubnets:")
        for subnet in subnets:
            print(subnet.id, "-", subnet.cidr_block)
    else:
        print("There is no subnet in this VPC!")


if __name__ == '__main__':
    main()
