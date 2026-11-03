# Assignment 5 - Jenkins + Docker + GitHub (Q1-20)

## Q1-3 Push app to GitHub
```bash
cd app && git init && git add . && git commit -m "Flask app + Dockerfile"
git branch -M main
git remote add origin https://github.com/<user>/jenkins-demo.git
git push -u origin main
git clone https://github.com/<user>/jenkins-demo.git ~/clone-test     # Q1 clone
```
## Q4 Prerequisite setup (one time, Ubuntu)
```bash
sudo usermod -aG docker jenkins      # lets Jenkins run docker commands (Q7)
sudo systemctl restart jenkins
sudo apt install -y python3 curl
```
## Freestyle jobs (New Item -> Freestyle). SCM: Git -> repo URL -> Branch `*/main`
| Q | Job | Execute shell |
|---|-----|---------------|
| 4/5 | gh_fetch | `ls -l; echo "Code fetched from GitHub"` |
| 6 | gh_python | `python3 hello.py` |
| 7 | docker_check | `docker --version` |
| 8 | docker_build | `docker build -t myapp .` |
| 9 | docker_run | `docker build -t myapp . && docker run -d --name myapp -p 5000:5000 myapp` |
| 10 | (same job) | edit app.py on GitHub (Version 2), click Build Now again, image rebuilds |
| 12 | branch_build | Branch Specifier `*/dev`, shell: `docker build -t myapp .` |
| 13 | tag_build | `docker build -t myapp:v1 .` |
| 14 | redeploy | `docker rm -f myapp \|\| true` then `docker build -t myapp:latest .` then `docker run -d --name myapp -p 5000:5000 myapp:latest` |

## Q11 Webhook
1. GitHub repo -> Settings -> Webhooks -> Add webhook
2. Payload URL: `http://<public-ip>:8080/github-webhook/` (Jenkins must be reachable; locally use `ngrok http 8080`)
3. Content type: application/json -> Just the push event
4. Jenkins job -> Configure -> Build Triggers -> tick *GitHub hook trigger for GITScm polling*

## Q15/16 Push to Docker Hub from Jenkins
1. Manage Jenkins -> Credentials -> Global -> Add -> *Username with password* -> ID `dockerhub` (Docker Hub user + access token)
2. Job -> Build Environment -> *Use secret text(s) or file(s)* -> Username and password (separated) -> Username var `DH_USER`, Password var `DH_PASS`, credential `dockerhub`
3. Execute shell:
```bash
docker build -t $DH_USER/myapp:v1 .
echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
docker push $DH_USER/myapp:v1
```
## Q17-20 Pipeline job
New Item -> *Pipeline* -> Pipeline script from SCM -> Git -> repo URL -> branch `*/main` -> Script Path `Jenkinsfile`.
Start with only the Hello+Checkout stages (Q17), add Build (Q18), then Deploy+Verify (Q19). Final Jenkinsfile in `app/` is Q20. Add the webhook from Q11 for full CI/CD: push -> auto build -> new container.
