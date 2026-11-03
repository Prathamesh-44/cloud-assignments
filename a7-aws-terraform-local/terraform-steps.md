# Assignment 7 - Terraform (local provider)
```bash
terraform -version        # Q1 (install: https://developer.hashicorp.com/terraform/install)
cd tf-local
terraform init
terraform plan
terraform apply -auto-approve
ls -l; cat hello.txt second.txt
terraform output
terraform destroy -auto-approve
```
Q2 = first resource only; Q3 = add `second`; Q4 = `variables.tf` + `terraform.tfvars`; Q5 = `outputs.tf`. The folder already contains the final version; to demo each step, comment out parts and re-apply.
