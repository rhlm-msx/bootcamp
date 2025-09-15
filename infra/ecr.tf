resource "aws_ecr_repository" "lambda_ecr" {
  name                 = "test"
  image_tag_mutability = "MUTABLE"
}

output "ecr_url" {
  value = aws_ecr_repository.lambda_ecr.repository_url
}
