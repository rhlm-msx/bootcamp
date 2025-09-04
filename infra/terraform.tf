terraform {
	required_providers {
		aws = {
			source = "hashicorp/aws"
			version = "~> 5.19"
		}
	}	

	required_version = ">= 1.2"

}

provider "aws" {
	region = "ap-south-1"
}


resource "aws_s3_bucket" "buck"{
}

output "buck_name_log" {
	value = aws_s3_bucket.buck.bucket
}
