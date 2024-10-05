import boto3
import os

session = boto3.Session(
    aws_access_key_id=os.getenv("Kassem-AWS-accesskey"),
    aws_secret_access_key=os.getenv("Kassem-AWS-secretaccesskey"),
    region_name="us-east-1"
)

s3 = session.client('s3')

def create_bucket(bucket_name, key_id):
    session_region =  session.region_name
        
    s3.create_bucket(Bucket=bucket_name)

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
                        'SSEAlgorithm': 'aws:kms',
                        'KMSMasterKeyID': 'key_id'
                    }
                }
            ]
        }
    )


if __name__ == "__main__":
    bucket_name = input("Enter the S3 bucket name: ")
    key_id = os.getenv('KMS-first-key-arn')

    create_bucket(bucket_name=bucket_name, key_id=key_id)