import os

class Creds:
    KEY = os.environ.get("AWS_ACCESS_KEY_ID", None)
    SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
    REGION = os.environ.get("AWS_REGION", None)
    ENDPOINT = os.environ.get("AWS_ENDOINT", "http://localhost:4566") 
