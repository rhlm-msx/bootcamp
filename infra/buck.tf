resource "aws_s3_bucket" "bucket"{
	acl = "private"
	
}

output "bucket_name" {
	value = aws_s3_bucket.bucket.bucket
}
