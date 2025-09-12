resource "aws_lambda_function" "docker_lambda" {
  function_name = "test_lambda"
  package_type  = "Image"
  image_uri     = "196980042128.dkr.ecr.ap-south-1.amazonaws.com/test_lambda:latest"
  role          = aws_iam_role.role.arn
}
