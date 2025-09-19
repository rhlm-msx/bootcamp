resource "aws_s3_bucket" "assets" {
}

resource "aws_s3_bucket_acl" "buck_acl" {
    bucket = aws_s3_bucket.assets.bucket
    acl = "private"
}

output "assets_bucket" {
    value = aws_s3_bucket.assets.bucket
}