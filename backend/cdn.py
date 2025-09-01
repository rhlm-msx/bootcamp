'''

Download file from S3.


'''
from creds import Creds
import boto3
from botocore.exceptions import ClientError
import logging

logging.basicConfig()
logger = logging.getLogger()

class Assets:
    def __init__(self, bucketname: str):
        self.bucketname = bucketname
        self.downloaded_files = set({})
        logger.info("Connecting to s3://{bucketname}.")
        self.s3_client = boto3.resource("s3", region_name=Creds.REGION, use_ssl=True, endpoint_url=Creds.ENDPOINT)
        self.s3b = self.s3_client.Bucket(bucketname)

    def fetchContent(self, key):
        logger.info("Extracting Key.")
        data = None
        if key in self.downloaded_files:
            with open(f"/tmp/{key}") as file:
                data = file.read()
        else:
            data = self.downloadContent(key)
        return data


    def downloadContent(self, key):
        data = None
        obj = self.s3b.Object(key)
        with open(f"/tmp/{key}", "wb") as file:
            try:
                obj.download_fileobj(file)
            except ClientError as e:
                logger.error(f"Key:{key} or Bucket:{self.bucketname} Not Found!!")
                return None
        self.downloaded_files.add(key)
        return self.fetchContent(key)


buck = Assets("locals3")
buck.fetchContent("wal.pdf")
