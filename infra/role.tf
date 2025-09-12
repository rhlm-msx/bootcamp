resource "aws_iam_role" "role" {
  name               = "lambda_role"
  assume_role_policy = data.aws_iam_policy_document.iam_policy.json
}

resource "aws_iam_role_policy" "lambda_s3_policy" {
	name 	= "lambda_policy_for_s3"
	role 	= aws_iam_role.role.id
	policy = data.aws_iam_policy_document.lambda_buck_access_policy.json

}
