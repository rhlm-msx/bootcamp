import os



MAIN_BUCKET_NAME = os.environ.get("BUCKET_NAME", None)
class Creds:
    KEY = os.environ.get("AWS_ACCESS_KEY_ID", None)
    SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
    REGION = os.environ.get("AWS_REGION", None)
    ENDPOINT = os.environ.get("AWS_ENDOINT", None)
