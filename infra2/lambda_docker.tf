resource "aws_lambda_function" "docker_lambda" {
  function_name = "test_lambda"
  package_type  = "Image"
  image_uri     = "196980042128.dkr.ecr.ap-south-1.amazonaws.com/test_lambda:latest"
  role          = aws_iam_role.role.arn
  environment {
	variables = {
		BUCKET_NAME = aws_s3_bucket.bucket.bucket
		STAGE = "dev"
		ENV = "aws"
	}

  }

}

resource "aws_lambda_function_url" "furl" {
  function_name      = aws_lambda_function.docker_lambda.function_name
  authorization_type = "NONE"
}

output "lambda_url" {
	value = aws_lambda_function_url.furl.function_url
}
