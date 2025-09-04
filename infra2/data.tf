data "archive_file" "code_repo" {
  type        = "zip"
  source_dir  = "../app"
  output_path = "./app.zip"

}

data "archive_file" "layer_repo" {
  type        = "zip"
  source_dir  = "../depend"
  output_path = "./layer.zip"

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


