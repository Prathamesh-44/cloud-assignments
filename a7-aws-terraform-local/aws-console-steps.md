# AWS Console (GUI) Steps

Covers Assignment 7 (EC2, S3, Lambda) and Self-Assignment 01 (Q1-6). Log in at https://console.aws.amazon.com and set the region (top right) to **Asia Pacific (Mumbai) ap-south-1**.

## 0. IAM user and access key (needed for AWS CLI and Terraform)
1. Search **IAM** -> Users -> **Create user** -> name `cdac-user`.
2. Set permissions -> Attach policies directly -> tick **AdministratorAccess** -> Create user.
3. Open the user -> **Security credentials** -> Create access key -> choose CLI -> copy both keys.
4. In the terminal run `aws configure` and paste the keys, region `ap-south-1`, output `json`.

## 1. EC2 (Assignment 7 Q1-5, Self Q1, Q6)

**Launch (Q1):** EC2 -> **Launch instance**
- Name: `my-server`
- AMI: **Amazon Linux 2023**
- Instance type: `t2.micro` or `t3.micro` (free tier)
- Key pair: Create new -> name `mykey` -> RSA, `.pem` -> Create (file downloads)
- Network settings: tick **Allow SSH** and **Allow HTTP traffic from the internet**
- Click **Launch instance**. Wait for State = *Running* and Status checks = *2/2 passed*.

**Connect (Q2):** select instance -> **Connect** -> *EC2 Instance Connect* tab -> **Connect**.

**Web server (Q3):** in that terminal:
```bash
sudo dnf install -y httpd
echo "<h1>Hello from EC2</h1>" | sudo tee /var/www/html/index.html
sudo systemctl enable --now httpd
```
Copy the **Public IPv4 address** and open `http://<ip>` (http, not https).

**Stop and start (Q4):** Instance state -> **Stop instance** (stopping -> stopped) -> Instance state -> **Start instance**. The public IP changes.

**Security group for port 80 (Q5):** EC2 -> Security Groups -> **Create security group** -> name `web-sg` -> Inbound rules -> Add rule: Type **HTTP**, Source **Anywhere-IPv4** -> Create.
If the page does not load: instance -> Security tab -> click the security group -> Edit inbound rules -> add HTTP 80.

## 2. S3 (Assignment 7 Q6-10, Self Q2)
- **Create bucket (Q6):** S3 -> **Create bucket** -> globally unique lowercase name (e.g. `prathamesh-cdac-2026`) -> region ap-south-1 -> keep Block Public Access on -> Create.
- **Upload 3 files (Q7):** open bucket -> **Upload** -> Add files (3) -> Upload. The **Objects** tab lists them.
- **Download (Q8):** tick a file -> **Download**.
- **Folder (Q9):** **Create folder** -> `docs` -> Create -> open it -> Upload 2 files.
- **Versioning (Q10):** bucket -> **Properties** -> Bucket Versioning -> Edit -> **Enable** -> Save. Upload `ver.txt`, change its text, upload again with the same name. On Objects tab turn on **Show versions**.
- **Permissions (Self Q2):** bucket -> **Permissions** tab. Keep Block Public Access on for private files. To show controlled access, tick the file -> Object actions -> **Share with a presigned URL**, or add a **Bucket policy**.

## 3. Lambda (Assignment 7 Q11-15, Self Q3)
1. Search **Lambda** -> **Create function** -> *Author from scratch*.
2. Name `hello-fn`, Runtime **Python 3.12** -> Create function.
3. Code tab: replace the code with a file from `a7-aws-terraform-local/lambda/` -> **Deploy**.
4. **Test** -> Create new event -> name `t1` -> paste JSON -> Save -> **Test**. Output shows under "Execution results".

Test JSON:
- `q12_sum.py`: `{"a": 4, "b": 6}` returns `{"sum": 10}`
- `q13_greeting.py`: `{"name": "Prathamesh"}`
- `q15_datetime.py`: `{}`
- Q14: run several different events on the same function and compare outputs.

## 4. VPC with public and private subnet (Self Q4, Q5)
1. Search **VPC** -> Your VPCs -> **Create VPC** -> *VPC only* -> Name `HPCSA-lab`, IPv4 CIDR `172.20.0.0/16` -> Create.
2. Subnets -> **Create subnet** -> VPC HPCSA-lab -> add two:
   - `public-subnet`: `172.20.5.0/24`
   - `private-subnet`: `172.20.10.0/24`
3. **Internet gateway:** Internet gateways -> Create `hpcsa-igw` -> Actions -> **Attach to VPC** -> HPCSA-lab.
4. **Public route table:** Route tables -> Create (VPC = HPCSA-lab) -> Routes -> Edit -> add `0.0.0.0/0` target = the internet gateway -> Save. Subnet associations -> Edit -> tick **public-subnet** -> Save. The private subnet stays on the default route table (no internet).
5. **Auto public IP:** select public-subnet -> Actions -> Edit subnet settings -> tick **Enable auto-assign public IPv4** -> Save.
6. **Security group:** Security Groups -> Create -> VPC HPCSA-lab, name `hpcsa-sg`. Inbound: SSH (22) from Anywhere, HTTP (80) from `172.20.0.0/16`.
7. **Launch two instances** (Launch instance -> Edit network settings): one in `public-subnet`, one in `private-subnet` (auto-assign public IP = Disable), both with `hpcsa-sg`.
8. **Web service on the private instance:** it has no internet, so `dnf install` fails. Simple demo: SSH to the public instance, then `ssh -i mykey.pem ec2-user@<private-ip>` (copy the `.pem` over first), then run `sudo python3 -m http.server 80`.
   If httpd is required: create a **NAT gateway** (VPC -> NAT gateways, in the public subnet, with an Elastic IP), add route `0.0.0.0/0 -> NAT` to the private subnet's route table, run `sudo dnf install -y httpd && sudo systemctl enable --now httpd`, then delete the NAT gateway afterwards (it costs money).
9. **Verify:** from the public instance run `curl http://<private-ip>`.

## 5. Clean up after every demo (avoid charges)
- EC2: select instance -> Instance state -> **Terminate**.
- NAT gateway: delete it, then release the Elastic IP.
- S3: **Empty** the bucket, then **Delete** it.
- Terraform resources: `terraform destroy -auto-approve`.
