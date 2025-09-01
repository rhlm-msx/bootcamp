#!/bin/python

import os
import boto3
from tqdm import tqdm



s3 = boto3.resource("s3", endpoint_url="http://localhost:4566")
cli = s3.Bucket("locals3")




dt_bt = 0
def callback(bt):
    global dt_bt
    dt_bt += bt


objs = set([obj.key for obj in cli.objects.all()])
lfiles = []

for p, s, files in os.walk("assets"):
    dirs = p.split("/")[1:]
    if len(dirs) > 0 and dirs[-1].startswith("."): continue;
    cd = "_".join(dirs)
    for name in files:
        if name.startswith("."): continue
        key = f"{cd}_{name}"
        path = f"{p}/{name}"
        lfiles += [(key, path)]

for key, path in tqdm(lfiles):
    if key not in objs:
        objs.add(key)
        cli.upload_file(path, key, Callback=callback)

print(f"Uploaded {dt_bt / (1024 * 1024):.2f}MB..")
