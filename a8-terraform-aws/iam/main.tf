# Q3 + Q7: IAM user with S3 read-only, IAM group, user added to group
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_iam_user" "u" {
  name = "tf-demo-user"
}

# Q3: attach AWS managed read-only S3 policy
resource "aws_iam_user_policy_attachment" "s3_ro" {
  user       = aws_iam_user.u.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

# Q7: group + membership
resource "aws_iam_group" "g" {
  name = "tf-demo-group"
}

resource "aws_iam_group_membership" "m" {
  name  = "tf-demo-membership"
  group = aws_iam_group.g.name
  users = [aws_iam_user.u.name]
}
