import dotenv
import os
import boto3
from botocore.config import Config as S3Config
import tqdm
import os


'''
Setup S3 Bucket

- Name of S3 Bucket.
- List of Images and Associated Identifiers.

Problem:
- File Overwritten


'''


AWS_ACCESS_KEY_ID    = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_KEY       = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
AWS_REGION           = os.environ.get("AWS_REGION", None)
AWS_OUT_FORMAT       = os.environ.get("AWS_OUT_FORMAT", None)
BUCKET_NAME          = os.environ.get("AWS_BUCKET_NAME", None)
ENDPOINT             = os.environ.get("ENDPOINT", None)


s3_conf = S3Config(region_name=AWS_REGION)

s3_client = boto3.client("s3", endpoint_url=ENDPOINT, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)

res = s3_client.create_bucket(Bucket=BUCKET_NAME)

if (res["ResponseMetadata"]["HTTPStatusCode"] == 200): 
    print("Sucesssfully Created!! Bucket")



print("Uploading File")
for p, s, f in os.walk("dataset/product_images"):
    for name in tqdm.tqdm(f):
        pid = name.split(".")[0]
        res = s3_client.upload_file(f"{p}/{name}", BUCKET_NAME, f"product_image_{pid}")

print("S3 Bucket Sucessfully Setup!!")




