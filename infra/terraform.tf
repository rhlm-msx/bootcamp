terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }
  }

  backend "s3" {
	bucket = "terraform-20250916064028048800000001"
	key = "final.terraform.tfstate"
	region = "ap-south-1"
  }

  required_version = ">= 1.2"

}


provider "aws" {
  region = "ap-south-1"
}




