resource "aws_ecr_repository" "test" {
  name                 = "test"
  image_tag_mutability = "MUTABLE"
}

output "ecr_url" {
  value = aws_ecr_repository.test.repository_url
}
