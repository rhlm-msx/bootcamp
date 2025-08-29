from typing import Annotated, List
import time
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import json
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
import pandas as pd
import subprocess
import boto3
from botocore.config import Config as S3Config
import dotenv
from functools import cache
import os
from mangum import Mangum
import uvicorn

AWS_ACCESS_KEY_ID   = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_KEY      = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
AWS_REGION          = os.environ.get("AWS_REGION", "ap-south-1")
AWS_OUT_FORMAT      = os.environ.get("AWS_OUT_FORMAT", "json")
ENDPOINT            = os.environ.get("ENDPOINT", None)
BUCKET_NAME         = os.environ.get("BUCKET_NAME", None)

assert AWS_ACCESS_KEY_ID != None, "AWS Credential Not Setup"
s3_conf = S3Config(region_name=AWS_REGION)
s3_client = boto3.client("s3", endpoint_url=ENDPOINT, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)
try:
    res = s3_client.head_bucket(Bucket=BUCKET_NAME)
except Exception as e:
    print(f"[ERROR]: Bucket {BUCKET_NAME}, is not setup, count or couldnt not connect, {e}")
    exit(-1)




products = pd.read_csv("dataset/products.csv")
products = products.set_index("id")
products["price"] = products["price"].map(lambda x: float(x[1:]))
main = FastAPI()
main.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

dsr_html = open("dsr/main.html").read()
main_html = open("main.html").read()
doorchart_html = open("products/index.html").read()


@cache
def get_images(id):
    res = s3_client.download_file(f"{BUCKET_NAME}", f"product_image_{id}", f"/tmp/pimg_{id}.png")
    return FileResponse(f"/tmp/pimg_{id}.png")



@main.get("/", response_class=HTMLResponse)
async def root():
    return main_html


@main.get("/doorchart", response_class=FileResponse)
async def doorchart():
    return FileResponse("products/index.html")


@main.get("/products", response_class=HTMLResponse)
async def product_page(min_price: int = 0):
    return products[products["price"] >= min_price].to_html()

@main.get("/products/main.js", response_class=HTMLResponse)
async def mainjs():
    return FileResponse("products/main.js")



@main.get("/products_csv", response_class=HTMLResponse)
async def product_page(min_price: int = 0):
    return products[products["price"] >= min_price].to_csv()



def notFoundResponse():
    return HTMLResponse(content='''
    <html>
    <head></head>
    <body>
        <h1>404: Not Found!</h1>
    </body>
    </html>
                        ''', status_code=404)

@main.get("/product_img/{id}")
async def fetch_image(id):
    if BUCKET_NAME == None:
        return notFoundResponse()
    try:
        return get_images(id)
    except:
        return notFoundResponse()

@main.get("/dsr", response_class=HTMLResponse)
async def dsr_page():
    return dsr_html




@main.get("/walmart")
async def wal():
    return FileResponse("main.pdf")




class JSONData(BaseModel):
    mentor: str
    week: int
    date: str
    res_chal: str
    ccl: str
    ndp: str
    work_done: List[str] | None = ["NA"]
    work_in_progress: List[str] | None = ["NA"]
    res_chal: List[str] | None = ["NA"]
    unres_chal: List[str] | None = ["NA"]

@main.post("/dsr")
async def dsr_main(data: JSONData):
    works = [ f"- {x.strip()}" for x in data.work_done]
    prog = [ f"- {x.strip()}" for x in data.work_in_progress ]
    res_chal = [ f"- {x.strip()}" for x in data.res_chal]
    unres_chal = [ f"- {x.strip()}" for x in data.unres_chal]
    yaml=f'''
---
mentor: {data.mentor}
week: {data.week}
report:
{"\n".join(works)}
{"\n".join(prog)}
rep-status:
{"\n".join([ "- Done" for _ in range(len(works))])}
{"\n".join([ "- In Progress" for _ in range(len(prog))])}
challenges:
{"\n".join(res_chal)}
{"\n".join(unres_chal)}
challenges-status:
{"\n".join([ "- Resolved" for _ in range(len(res_chal))])}
{"\n".join([ "- Unresolved" for _ in range(len(unres_chal))])}
resolution:
  - {data.res_chal}
references:
  - "Github: PAT": "https://www.youtube.com/watch?v=IuiH6cBtc58"
  - "PAT Docs": "https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2022-11-28"
commits:
next:
{"\n".join([ f"- {x}" for x in data.ndp.split("\n")])}
'''
    fname = "dsr.yaml"
    with open(f"dsr/{fname}", "w") as file:
        file.write(yaml)
    subprocess.run(["sh", "-c","cd dsr && ./typst compile dsr.typ"])
    return FileResponse("dsr/dsr.pdf")

handler = Mangum(main)
