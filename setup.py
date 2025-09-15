#!/bin/python

import logging
import json
import os
import boto3
from hashlib import md5
from tqdm import tqdm




bucketname = os.environ.get("BUCKET_NAME", None)
endpoint_url = os.environ.get("AWS_ENDPOINT", None)
if bucketname == None:
    logging.error(f"BUCKET_NAME ENV not set")
    exit(-1)
if endpoint_url == None:
    logging.info("Connecting to Localstack")
else:
    logging.info("Connecting to AWS Servers")
s3 = boto3.resource("s3", endpoint_url=endpoint_url)
cli = s3.Bucket(bucketname)

logs = {}
try:
    with open(f"{bucketname}_logs") as file:
        logs = json.load(file)
except Exception as e:
    print("Log not exist")



dt_bt = 0
def callback(bt):
    global dt_bt
    dt_bt += bt


existing_keys = set([obj.key for obj in cli.objects.all()])
dir_files = {}
dir_file_keys = set([])


moded = []

for p, s, files in os.walk("assets"):
    dirs = p.split("/")[1:]
    if len(dirs) > 0 and dirs[-1].startswith("."): continue;
    cd = "_".join(dirs)
    for name in files:
        if name.startswith("."): continue
        key = (cd if len(cd) == 0 else f"{cd}_") + name
        path = f"{p}/{name}"
        dir_files[key] = path
        dir_file_keys.add(key)
        with open(path, "rb") as file:
            h = md5(file.read()).hexdigest()
            oh = logs.get(key, "")
            if h != oh and key in existing_keys:
                existing_keys.remove(key)
                logs[key] = h

objs_to_delete = existing_keys - dir_file_keys
objs_to_upload = dir_file_keys - existing_keys

print(f"{len(objs_to_delete)}: Objects to delete")
print(f"{len(objs_to_upload)}: Objects to upload")

if len(objs_to_delete) > 0:
    cli.delete_objects(Delete = {
        "Objects":list(map( lambda x: {"Key": x}, objs_to_delete))
    })


for key in tqdm(objs_to_upload):
    cli.upload_file(dir_files[key], key, Callback=callback)
with open(f"{bucketname}_logs", "w") as file:
    json.dump(logs, file)

print(f"Uploaded {dt_bt / (1024 * 1024):.2f}MB..")
