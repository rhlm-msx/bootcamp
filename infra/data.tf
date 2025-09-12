data "archive_file" "code_repo" {
  type        = "zip"
  source_dir  = "../app"
  output_path = "./app.zip"

}

data "archive_file" "layer_repo1" {
  type        = "zip"
  source_dir  = "../depend1"
  output_path = "./layer1.zip"

}


data "archive_file" "layer_repo2" {
  type        = "zip"
  source_dir  = "../depend2"
  output_path = "./layer2.zip"

}

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


