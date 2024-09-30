import os
import boto3

session = boto3.Session(
        aws_access_key_id=os.getenv("Kassem-AWS-accesskey"),
        aws_secret_access_key=os.getenv("Kassem-AWS-secretaccesskey"),
        region_name="me-central-1"
    )


iam = session.client('iam')

def add_user_to_group(username):
    iam.add_user_to_group(GroupName='file-store-group',
                          UserName=username,)

if __name__ == '__main__':
    username = input("Enter the users name: ")
    add_user_to_group(username=username)