'''

1. Establish Connection with S3
2. Extract Relevant Content from S3
3. Send them to client


'''


import os
import boto3
from botocore.config import Config


class Creds:
    KEY = "DEFAULT"
    SECRET = ""
    REGION = ""
    FORMAT = "json"
    ENDPOINT = ""
    BUCKET_NAME = ""

    def loadfromEnv():
        Creds.KEY = os.environ.get("AWS_ACCESS_KEY_ID", None)
        Creds.SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
        Creds.REGION = os.environ.get("AWS_REGION", "ap-south-1")
        Creds.FORMAT = os.environ.get("AWS_OUT_FORMAT", "json")
        Creds.ENDPOINT = os.environ.get("ENDPOINT", None)
        Creds.BUCKET_NAME = os.environ.get("BUCKET_NAME", None)



