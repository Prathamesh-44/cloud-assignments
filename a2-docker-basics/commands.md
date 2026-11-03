# Assignment 2 Q4-8 (Docker)

Replace `<dockerhub-user>` with your Docker Hub username. Run `docker login` once.

## Q4: Factorial image + container
```bash
cd factorial-v1
docker build -t my-java-app .
docker run -it --rm my-java-app          # -it needed because program reads input
```
## Q5: Push to Docker Hub
```bash
docker tag my-java-app <dockerhub-user>/my-java-app:latest
docker push <dockerhub-user>/my-java-app:latest
```
## Q6 + Q7: Largest of 3 as version 2
```bash
cd ../largest-v2
docker build -t my-java-app:2 .
docker run -it --rm my-java-app:2
docker tag my-java-app:2 <dockerhub-user>/my-java-app:2
docker push <dockerhub-user>/my-java-app:2
```
## Q8: Apache web server
```bash
docker run -d --name apache -p 8080:80 httpd:latest
# browser: http://localhost:8080  -> "It works!"
docker stop apache && docker rm apache
```
