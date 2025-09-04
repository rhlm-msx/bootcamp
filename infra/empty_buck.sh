#!/bin/bash
objs=$(awslocal s3api list-objects --bucket "$1" | jq '.Contents.[].Key' -r)
data=$(echo $objs | python -c 'import sys;import json; print(json.dumps({"Objects": [ {"Key":x} for x in  sys.stdin.read().split()]}))')
awslocal s3api delete-objects --bucket locals3 --delete "$data"
