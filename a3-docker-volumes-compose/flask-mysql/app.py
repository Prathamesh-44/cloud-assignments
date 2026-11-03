# Inserts name + phone into MySQL table "mydata" (Assignment 3 Q3/Q4)
import os, time
import mysql.connector

cfg = dict(host=os.getenv("DB_HOST", "mysql-db"), user="root",
           password=os.getenv("DB_PASS", "root123"))

# MySQL takes a few seconds to start, so retry
for _ in range(30):
    try:
        conn = mysql.connector.connect(**cfg)
        break
    except mysql.connector.Error:
        print("Waiting for MySQL..."); time.sleep(3)
else:
    raise SystemExit("MySQL not reachable")

cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS mydb")
cur.execute("USE mydb")
cur.execute("CREATE TABLE IF NOT EXISTS mydata (name VARCHAR(50), phone VARCHAR(15))")
cur.execute("INSERT INTO mydata VALUES (%s, %s)", ("YourName", "9999999999"))
conn.commit()
print("Inserted row into mydata")
conn.close()
