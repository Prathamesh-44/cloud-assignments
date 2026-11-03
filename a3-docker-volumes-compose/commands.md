# Assignment 3

## Q1: Tomcat on port 9999
```bash
docker run -d --name tomcat -p 9999:8080 tomcat:9.0
# browser: http://localhost:9999   (404 page from Tomcat = server is running)
docker rm -f tomcat
```
## Q2: Apache + volume to change home page
```bash
mkdir -p ~/site && echo "<h1>Welcome to C-DAC</h1>" > ~/site/index.html
docker run -d --name apache -p 9999:80 -v ~/site:/usr/local/apache2/htdocs/ httpd:latest
# browser: http://localhost:9999  -> Welcome to C-DAC
echo "<h1>Hello Everyone</h1>" > ~/site/index.html
# refresh browser -> Hello Everyone (no restart needed)
docker rm -f apache
```
## Q3: Python app + MySQL in two containers, same network
```bash
docker network create mynet
docker run -d --name mysql-db --network mynet -e MYSQL_ROOT_PASSWORD=root123 mysql:8
cd flask-mysql
docker build -t pyapp .
docker run --rm --network mynet pyapp
docker exec -it mysql-db mysql -uroot -proot123 -e "SELECT * FROM mydb.mydata;"
```
## Q4: Same with a volume on MySQL
```bash
docker rm -f mysql-db
docker volume create mysqldata
docker run -d --name mysql-db --network mynet -v mysqldata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql:8
docker run --rm --network mynet pyapp
docker rm -f mysql-db                                   # remove container
docker run -d --name mysql-db --network mynet -v mysqldata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql:8
docker exec -it mysql-db mysql -uroot -proot123 -e "SELECT * FROM mydb.mydata;"   # data still there
```
## Q5: Compose hello
```bash
cd compose-hello && docker compose up --build
docker compose down
```
