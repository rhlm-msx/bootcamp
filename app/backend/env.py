import os
import logging


MAIN_BUCKET_NAME = os.environ.get("BUCKET_NAME", None)
KEY = os.environ.get("AWS_ACCESS_KEY_ID", None)
SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
REGION = os.environ.get("AWS_REGION", None)
ENDPOINT = os.environ.get("AWS_ENDPOINT", None)

if MAIN_BUCKET_NAME == None: 
    logging.warn("BUCKET_NAME ENV not set!!")

if KEY == None:
    logging.warn("AWS_ACCESS_KEY_ID ENV not set!!")

if SECRET == None:
    logging.warn("AWS_SECRET_ACCESS_KEY ENV not set!!")

if ENDPOINT == None:
    logging.info("Endpoint is AWS Servers")
else:
    logging.info("Endpoint is LocalStack")
