# Self-Assignments 01 and 02 - where to find each answer

| Q | Topic | Where |
|---|-------|-------|
| 1 | EC2 launch | `../a7-aws-terraform-local/aws-console-and-cli.md` (EC2) |
| 2 | S3 upload/download/permissions | same file (S3). Permissions: `aws s3api put-object-acl --bucket B --key f1.txt --acl private` or bucket policy in Console |
| 3 | Lambda Python | `../a7-aws-terraform-local/lambda/` |
| 4,5 | VPC HPCSA-lab, public+private EC2, httpd | `vpc-terraform/` (or Console). Steps below |
| 6 | Web app on EC2 | Install httpd (Q3 of A7) or run the Flask Docker image; open port 80 in security group |
| 7 | Two VMs with hypervisor | Steps below |
| 8 | OpenStack architecture | Write-up outline below |
| 9 | Multi-tenant DB | `multitenant/multitenant.py` -> `python3 multitenant.py` |
| 10, 11 | Git | `../a1-git/commands.md` |
| 12 | Dockerfile hello | `docker-web/` -> `docker build -f Dockerfile.hello -t hello . && docker run hello` |
| 13 | Dockerized Flask | `../a4-jenkins-docker/flask-student/` |
| 14 | Web + MySQL + volume | `../a3-docker-volumes-compose/commands.md` Q4 or `../a4-jenkins-docker/compose-flask-mysql/` |
| 15-17 | Kubernetes | `k8s/` |
| 18 | Jenkins hello + GitHub repo job | `../a4-jenkins-docker/jenkins-freestyle-steps.md` |
| 19 | Jenkins -> Docker Hub | `../a5-jenkins-cicd/jenkins-steps.md` (Q15/16) |
| 20 | Terraform EC2+VPC | `vpc-terraform/` |

## Q4/Q5 via Terraform (recommended)
```bash
cd vpc-terraform && terraform init && terraform apply -auto-approve
terraform output
# connect to public-ec2 (EC2 Instance Connect), then to private-ec2 via its private IP.
# Private instance has no internet, so install httpd on it by temporarily adding a NAT gateway,
# or do the Q5 demo with Python: on private-ec2 run `python3 -m http.server 80` (python3 is preinstalled on Amazon Linux).
# From public-ec2:  curl http://<private-ip>
terraform destroy -auto-approve
```
## Q7 Two VMs (VirtualBox)
1. Install VirtualBox; create 2 Ubuntu VMs.
2. VM Settings -> Network -> Adapter 1: *Internal Network* (name `labnet`) or *Host-only*; Adapter 2: NAT (for internet).
3. Inside each VM set static IPs (e.g. 192.168.50.11 and .12) with `sudo ip addr add 192.168.50.11/24 dev enp0s8` (adjust interface name via `ip a`).
4. `ping 192.168.50.12` from VM1 -> replies prove communication.
## Q8 OpenStack write-up outline
Keystone (identity), Nova (compute), Glance (images), Neutron (networking), Cinder (block storage), Swift (object storage), Horizon (dashboard), Heat (orchestration). Compute = Nova schedules VMs on hypervisors; storage = Cinder volumes / Swift objects; networking = Neutron virtual networks, routers, security groups. Compare each with the AWS equivalent (EC2, EBS, S3, VPC, IAM).
