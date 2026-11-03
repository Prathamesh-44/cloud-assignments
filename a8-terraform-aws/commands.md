# Assignment 8 - Terraform on AWS
Prerequisites: `aws configure` done (IAM user with admin or EC2/S3/IAM rights), Terraform installed.

Folder map:
- `ec2/`         -> Q1, Q4, Q5, Q9, Q10
- `s3/`          -> Q2, Q6, Q9
- `iam/`         -> Q3, Q7
- `ec2-s3-role/` -> Q8, Q9, Q10

Run in each folder:
```bash
terraform init
terraform validate
terraform plan
terraform apply -auto-approve
terraform destroy -auto-approve        # ALWAYS destroy after the demo to avoid charges
```
Q9 override variables without editing files:
`terraform apply -var="instance_type=t3.small" -var="region=ap-south-1"`

Q10: apply with `t3.micro`, then change `instance_type` to `t3.small` and `terraform plan` (shows "update in-place" or "replace") then `terraform apply`.
Change `bucket_name` in `s3/variables.tf` to something globally unique first.
