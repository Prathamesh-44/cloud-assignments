# Q8 + Q10: EC2 with IAM role giving S3 access; modify instance_type and re-apply
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = var.region
}

data "aws_ssm_parameter" "al2023" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
}

resource "aws_s3_bucket" "b" {
  bucket = var.bucket_name
}

resource "aws_iam_role" "ec2_role" {
  name = "tf-ec2-s3-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "s3" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

# EC2 attaches roles through an instance profile
resource "aws_iam_instance_profile" "profile" {
  name = "tf-ec2-s3-profile"
  role = aws_iam_role.ec2_role.name
}

resource "aws_instance" "app" {
  ami                  = data.aws_ssm_parameter.al2023.value
  instance_type        = var.instance_type
  iam_instance_profile = aws_iam_instance_profile.profile.name
  tags                 = { Name = "tf-role-instance" }
}
