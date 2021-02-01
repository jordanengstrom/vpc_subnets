"""
1st-Iteration Exercise:
Create an executable script that will use the AWS CLI to print the CIDR blocks of the VPC and of all subnets
in it.
"""

import awscliv2
import boto3
import sys


def main():
    # TODO: get CIDR blocks (CIDR = Classless Inter-Domain Routing)
    print('Please supply a VPC ID: ')
    vpc_id = input()

    print("Using VPC ID:", vpc_id)

    # Get EC2 resource
    ec2 = boto3.resource('ec2')

    # Get VPC resource using Ec2 resource by supplying VPC ID
    vpc = ec2.Vpc(vpc_id)
    print("VPC CIDR:", vpc.cidr_block)

    # Check whether VPC has subnets and display them accordingly
    subnets = list(vpc.subnets.all())
    # TODO: print available subnets
    if len(subnets) > 0:
        print("\nSubnets:")
        for subnet in subnets:
            print(subnet.id, "-", subnet.cidr_block)
    else:
        print("There is no subnet in this VPC!")


if __name__ == '__main__':
    main()
