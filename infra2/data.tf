data "aws_iam_policy_document" "iam_policy" {
  statement {

    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }

}


data "aws_iam_policy_document" "lambda_buck_access_policy" {

	statement {
		effect = "Allow"
		resources = [ aws_s3_bucket.bucket.arn, "${aws_s3_bucket.bucket.arn}/*"]
		actions = ["s3:GetObject", "s3:ListBucket"]
	}

}


