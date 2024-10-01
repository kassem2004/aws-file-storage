import os
import boto3

session = boto3.Session(
    aws_access_key_id=os.getenv('Kassem-AWS-accesskey-2'),
    aws_secret_access_key=os.getenv('Kassem-AWS-secretaccesskey-2'),
    region_name='us-east-1'
)

s3 = session.client('s3')

def add_object(bucket_name, file_path, key):
    file_data = open(file_path, 'rb')
    s3.put_object(
        Bucket=bucket_name,
        Body=file_data,
        Key=key,
        ServerSideEncryption='AES256'
    )

if __name__ == '__main__':
    bucket_name = input("Enter the bucket name: ")
    file_path = input("Enter the file path from you file explorer: ")
    key = input("Enter the object key (file path you the object to have in the bucket): ")

    add_object(bucket_name=bucket_name, file_path=file_path, key=key)