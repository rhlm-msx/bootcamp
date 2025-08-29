

resource "aws_lambda_function" "test_tf" {

  function_name = "test_tf"
  filename      = data.archive_file.code_repo.output_path
  runtime       = "python3.12"
  role          = resource.aws_iam_role.role.arn
  handler       = "app.handler"

  source_code_hash = md5(filebase64(data.archive_file.code_repo.output_path))

}

resource "aws_lambda_function_url" "furl" {
  function_name      = aws_lambda_function.test_tf.function_name
  authorization_type = "NONE"
}

output "lambda_url" {
	value = aws_lambda_function_url.furl.function_url
}
