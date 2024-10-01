import boto3
import os

session = boto3.Session(
    aws_access_key_id=os.getenv("Kassem-AWS-accesskey"),
    aws_secret_access_key=os.getenv("Kassem-AWS-secretaccesskey"),
    region_name="us-east-1"
)

iam = session.client('iam')

def create_iam_user(username):
    iam.create_user(UserName=username,
                    PermissionsBoundary='arn:aws:iam::aws:policy/AmazonS3FullAccess')
    policy_arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
    iam.attach_user_policy(UserName=username, PolicyArn=policy_arn)
    
if __name__ == "__main__":
    username = input("Enter the username you would like to add: ")
    create_iam_user(username=username)