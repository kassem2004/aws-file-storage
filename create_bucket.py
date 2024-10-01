import boto3
import os

session = boto3.Session(
    aws_access_key_id=os.getenv("Kassem-AWS-accesskey"),
    aws_secret_access_key=os.getenv("Kassem-AWS-secretaccesskey"),
    region_name="us-east-1"
)

s3 = session.client('s3')

def create_bucket(bucket_name):
    session_region =  session.region_name

    if session_region == 'us-east-1':
        s3.create_bucket(Bucket=bucket_name)
    else :
        s3.create_bucket(Bucket=bucket_name,
                     CreateBucketConfiguration={
                     'LocationConstraint': 'us-east-1'
                     }
                     )

    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )

    s3.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                }
            ]
        }
    )


if __name__ == "__main__":
    bucket_name = input("Enter the S3 bucket name: ")

    create_bucket(bucket_name=bucket_name)