resource "aws_lambda_function" "lambda" {
	function_name = "lambda"
	role = aws_iam_role.lambda_role.arn
	package_type = "Image"
	image_uri = "${aws_ecr_repository.lambda_ecr.repository_url}:latest"



	image_config {
		command = ["entry.handler"]
	}

	environment {
		variables = {
			ENV = "dev"
			BUCKET_NAME = "locals3"
		}
	}


	architectures = ["x86_64"]


}



resource "aws_lambda_function_url" "furl" {
	function_name = aws_lambda_function.lambda.function_name
	authorization_type = "NONE"
}

output "function_url" {

value = aws_lambda_function_url.furl.function_url

}
