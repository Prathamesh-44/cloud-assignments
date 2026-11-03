# Assignment 4 - Docker labs (Q1-10)

## Q1 Flask student page
```bash
cd flask-student
docker build -t student-app .
docker run -d --name student -p 5000:5000 student-app      # http://localhost:5000
```
## Q2 Java + MySQL
```bash
docker network create labnet
docker run -d --name mysql-db --network labnet -e MYSQL_ROOT_PASSWORD=root123 mysql:8
cd java-mysql && docker build -t java-db . && docker run --rm --network labnet java-db
```
## Q3 MySQL with named volume
```bash
docker volume create sqldata
docker run -d --name m1 -v sqldata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql:8
sleep 20
docker exec -it m1 mysql -uroot -proot123 -e "CREATE DATABASE school; USE school; CREATE TABLE t(id INT,name VARCHAR(20)); INSERT INTO t VALUES (1,'A'),(2,'B');"
docker rm -f m1
docker run -d --name m2 -v sqldata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql:8
sleep 20
docker exec -it m2 mysql -uroot -proot123 -e "SELECT * FROM school.t;"      # data retained
```
## Q4 Custom network, Flask -> MySQL by container name
```bash
docker network create flasknet
docker run -d --name db --network flasknet -e MYSQL_ROOT_PASSWORD=root123 mysql:8
cd compose-flask-mysql && docker build -t flask-db .
docker run -d --name web --network flasknet -p 5000:5000 -e DB_HOST=db flask-db    # host = container name "db"
```
## Q5 + Q9 Compose (Flask + MySQL, ports, env vars, named volume, 5 records)
```bash
cd compose-flask-mysql
docker compose up -d --build        # http://localhost:5000 shows 5 students
docker compose down
```
## Q6 Versioned images
```bash
cd flask-student
docker build -t student-app:1.0 .
sed -i 's/Your Name/Updated Name/' app.py
docker build -t student-app:2.0 .
docker run -d --name v1 -p 5001:5000 student-app:1.0
docker run -d --name v2 -p 5002:5000 student-app:2.0     # compare :5001 and :5002
```
## Q7 requirements.txt (no Python on host needed)
Already how flask-student/Dockerfile works: `COPY requirements.txt` + `RUN pip install -r requirements.txt`.
## Q8 Nginx with host directory
```bash
mkdir -p ~/nginxsite && echo "<h1>My Custom Page</h1>" > ~/nginxsite/index.html
docker run -d --name nginx1 -p 8081:80 -v ~/nginxsite:/usr/share/nginx/html:ro nginx
```
## Q10 Logs, stats, crashed container
```bash
docker run -d --name crashy busybox sh -c "echo starting; sleep 3; exit 1"
sleep 5
docker ps -a                 # crashy shows Exited (1)
docker logs crashy
docker start crashy          # restart
docker stats --no-stream     # resource usage of running containers
docker inspect crashy --format '{{.State.ExitCode}}'
# working app check: docker run -d --name ok -p 8082:80 nginx && curl -I localhost:8082
```
