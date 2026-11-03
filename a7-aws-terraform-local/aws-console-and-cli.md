# Assignment 7 - EC2, S3, Lambda (Console + CLI)
Install CLI per course slides, then `aws configure` (IAM user access key, region e.g. ap-south-1).

## EC2 (Q1-5)
Console: EC2 -> Launch instance -> Amazon Linux 2023 -> t2.micro/t3.micro -> create key pair -> Launch.
```bash
aws ec2 describe-instance-status --include-all-instances      # Q1 status
chmod 400 mykey.pem && ssh -i mykey.pem ec2-user@<public-ip>  # Q2 (or Console -> Connect -> EC2 Instance Connect)
# Q3 on the instance:
sudo dnf install -y httpd
echo "<h1>Hello from EC2</h1>" | sudo tee /var/www/html/index.html
sudo systemctl enable --now httpd
# Q4
aws ec2 stop-instances  --instance-ids i-xxxx     # state: stopping -> stopped
aws ec2 start-instances --instance-ids i-xxxx     # pending -> running (public IP changes!)
# Q5 security group allowing HTTP
aws ec2 create-security-group --group-name web-sg --description "HTTP" 
aws ec2 authorize-security-group-ingress --group-name web-sg --protocol tcp --port 80 --cidr 0.0.0.0/0
```
## S3 (Q6-10)  (bucket names are global: add something unique)
```bash
aws s3 mb s3://yourname-cdac-bucket-2026                              # Q6
echo a > f1.txt; echo b > f2.txt; echo c > f3.txt
aws s3 cp f1.txt s3://yourname-cdac-bucket-2026/ ; aws s3 cp f2.txt s3://yourname-cdac-bucket-2026/ ; aws s3 cp f3.txt s3://yourname-cdac-bucket-2026/
aws s3 ls s3://yourname-cdac-bucket-2026/                             # Q7
aws s3 cp s3://yourname-cdac-bucket-2026/f1.txt ./downloaded.txt      # Q8
aws s3api put-object --bucket yourname-cdac-bucket-2026 --key docs/   # Q9 folder
aws s3 cp f1.txt s3://yourname-cdac-bucket-2026/docs/ ; aws s3 cp f2.txt s3://yourname-cdac-bucket-2026/docs/
aws s3api put-bucket-versioning --bucket yourname-cdac-bucket-2026 --versioning-configuration Status=Enabled   # Q10
echo v1 > ver.txt; aws s3 cp ver.txt s3://yourname-cdac-bucket-2026/
echo v2 > ver.txt; aws s3 cp ver.txt s3://yourname-cdac-bucket-2026/
aws s3api list-object-versions --bucket yourname-cdac-bucket-2026 --prefix ver.txt
```
## Lambda (Q11-15): Console -> Lambda -> Create function -> Author from scratch -> Python 3.12 -> paste code -> Deploy -> Test.
Test events (Q14): `{"a": 4, "b": 6}`, `{"a": -1, "b": 1}`, `{"name": "Asha"}`, `{}`.
Code: see `lambda/*.py`.
