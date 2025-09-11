resource "aws_iam_role" "role" {
  name               = "lambda_role"
  assume_role_policy = data.aws_iam_policy_document.iam_policy.json
}
