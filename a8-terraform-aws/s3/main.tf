# Q2 + Q6 + Q9: S3 bucket, versioning, sample file upload
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "b" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_versioning" "v" {
  bucket = aws_s3_bucket.b.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_object" "sample" {
  bucket  = aws_s3_bucket.b.id
  key     = "sample.txt"
  content = "Hello from Terraform"
}
