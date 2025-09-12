import pytest
from entry import handler


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
    "path": path,
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
    print(handler)
    res = handler(event, context)
    assert res["statusCode"] == 307


def test_app(make_event, context):
    event = make_event("GET", "/app")
    res = handler(event, context)
    print(res)
    assert res["statusCode"] == 200

