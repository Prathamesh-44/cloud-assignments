FROM eclipse-temurin:17-jdk
WORKDIR /app
# Download the MySQL JDBC driver at build time
ADD https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.4.0/mysql-connector-j-8.4.0.jar /app/mysql.jar
COPY DbApp.java .
RUN javac DbApp.java
CMD ["java", "-cp", ".:mysql.jar", "DbApp"]
