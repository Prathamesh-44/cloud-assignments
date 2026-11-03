# Cloud Computing Assignments (C-DAC)

Everything for Assignments 1-8 and Self-Assignments 1-2, organised by folder. Each folder has code plus a `commands.md` / `*-steps.md` with the exact commands in order.

| Folder | Covers |
|--------|--------|
| `a1-git/` | Git PDF assignment, branches, conflict, PR, stash/revert |
| `a2-docker-basics/` | Java factorial image, v2 largest-of-3, Docker Hub, Apache |
| `a3-docker-volumes-compose/` | Tomcat, Apache volume, Python+MySQL, volumes, Compose |
| `a4-jenkins-docker/` | 10 Jenkins freestyle jobs + 10 Docker labs |
| `a5-jenkins-cicd/` | Jenkins + GitHub + Docker, Jenkinsfile, CI/CD pipeline |
| `a6-kubernetes/` | Pods, ReplicaSet, Deployment, failure cases |
| `a7-aws-terraform-local/` | EC2/S3/Lambda, Terraform local provider |
| `a8-terraform-aws/` | Terraform for EC2, S3, IAM |
| `self-assignment/` | VPC, multi-tenancy, K8s service, OpenStack, mapping table |

## Prerequisites (Ubuntu, as in the course slides)
Git, Docker Engine, minikube, Jenkins, AWS CLI + `aws configure`, Terraform.

## Push to GitHub
```bash
cd cloud-assignments
git init && git add . && git commit -m "Cloud computing assignments"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo>.git
git push -u origin main
```
**Cost warning:** run `terraform destroy` after every AWS demo.
**Before demo:** replace `Your Name`, phone, `<dockerhub-user>`, and unique S3 bucket names.
