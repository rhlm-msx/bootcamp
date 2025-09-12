import pytest
import time
import json
from entry import handler
from http import HTTPStatus



def get_event(method="GET", path="/", query="", body=None, content_type="", content_length=0) :
    extract_query = {}
    if len(query) > 0:
        params = [ list(map(lambda x: x.strip(), field.split("="))) for field in query.split("&") ]
        extract_query = { param[0]:param[1] for param in params }
    return {
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": path,
  "rawQueryString": query,
  "headers": {
    "sec-fetch-mode": "navigate",
    "x-amzn-tls-version": "TLSv1.3",
    "sec-fetch-site": "none",
    "x-forwarded-proto": "https",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "x-forwarded-port": "443",
    "x-forwarded-for": "103.80.163.162",
    "sec-fetch-user": "?1",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "x-amzn-tls-cipher-suite": "TLS_AES_128_GCM_SHA256",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "x-amzn-trace-id": "Root=1-68c3fa1b-15e119cf6f188384122031d2",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "host": "q4igi5bnp2vmnn4avp5qpffboe0xbxox.lambda-url.ap-south-1.on.aws",
    "upgrade-insecure-requests": "1",
    "accept-encoding": "gzip, deflate, br, zstd",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "sec-fetch-dest": "document",
    "Content-Type": content_type,
    "Content-Length": f"{content_length}",
  },
  "queryStringParameters": extract_query,
  "requestContext": {
    "accountId": "anonymous",
    "apiId": "q4igi5bnp2vmnn4avp5qpffboe0xbxox",
    "domainName": "q4igi5bnp2vmnn4avp5qpffboe0xbxox.lambda-url.ap-south-1.on.aws",
    "domainPrefix": "q4igi5bnp2vmnn4avp5qpffboe0xbxox",
    "http": {
      "method": method,
      "path": path,
      "protocol": "HTTP/1.1",
      "sourceIp": "103.80.163.162",
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    },
    "requestId": "12f53a84-afee-4200-8797-4597d1db6ba2",
    "routeKey": "$default",
    "stage": "$default",
    "time": time.strftime("%d/%b/%Y:%H:%M:%S +0000"),
    "timeEpoch": int(time.time() * 1000)
  },
  "isBase64Encoded": False,
  "body": None
}


class Context:
    function_name = "lambda_docker"
    memory_limit_in_mb = 128
    invoked_function_arn = "arn:aws:lambda:local:test"
    aws_request_id = "req_id"


@pytest.fixture
def context():
    return Context()




@pytest.fixture
def make_event():
    return get_event

def test_root(make_event, context):
    event = make_event("GET", "/")
    res = handler(event, context)
    assert res["statusCode"] == HTTPStatus.TEMPORARY_REDIRECT.value


def test_app(make_event, context):
    event = make_event("GET", "/app")
    res = handler(event, context)
    assert res["statusCode"] == HTTPStatus.OK.value

def test_app2(make_event, context):
    event = make_event("GET", "/app/")
    res = handler(event, context)
    assert res["statusCode"] == HTTPStatus.OK.value


def test_not_exist(make_event, context):
    event = make_event("GET", "/canyoufindthewaldoalongwithshaktimaan")
    res = handler(event, context)
    assert res["statusCode"] == HTTPStatus.NOT_FOUND.value

def test_summary(make_event, context):
    event = make_event("GET", "/inventory/summary")
    res = handler(event, context)
    print(res)
    assert res["statusCode"] == HTTPStatus.OK.value
    assert res["headers"]["content-type"] == "application/json"
    assert json.loads(res["body"])["entity_count"] >= 0

