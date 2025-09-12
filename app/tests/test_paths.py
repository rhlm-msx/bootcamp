import pytest
import json
from entry import handler
from http import HTTPStatus


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
    def __make_event(method="GET", path="/", query="", body=None):
        return {
  "resource": path,
  "path": path,
  "httpMethod": method,
  "headers": {
    "Accept": "*/*",
    "Host": "localhost"
  },
  "queryStringParameters": {
  },
  "pathParameters": None,
  "stageVariables": None,
  "requestContext": {
    "resourceId": "123456",
    "resourcePath": path,
    "httpMethod": method,
    "extendedRequestId": "REQUEST_ID",
    "identity": {
      "cognitoIdentityPoolId": None,
      "accountId": None,
      "cognitoIdentityId": None,
      "caller": None,
      "sourceIp": "127.0.0.1",
      "principalOrgId": None,
      "accessKey": None,
      "cognitoAuthenticationType": None,
      "cognitoAuthenticationProvider": None,
      "userArn": None,
      "userAgent": "PostmanRuntime/7.26.8",
      "user": None
    },
    "accountId": "123456789012",
    "protocol": "HTTP/1.1",
    "apiId": "abcdefg"
  },
  "body": None,
  "isBase64Encoded": False
}
        return {
                "resource": path,
                "httpmethod": method,
                "path": path,
                "version": "2.0",
                "routeKey": f"{method} {path}",
                "rawPath": path,
                "rawQueryString": query,
                "headers": {
                    "Host": "localhost",
                    "user-agent": "test",
                },
                "requireContext": {
                    "http": {
                        "method": method,
                        "path": path
                        }
                },
                "isBase64Encoded": False,
                "body": body

        }
    return __make_event

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

