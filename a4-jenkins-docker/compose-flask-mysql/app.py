import os, time
import mysql.connector
from flask import Flask

app = Flask(__name__)


def get_conn():
    return mysql.connector.connect(host=os.getenv("DB_HOST", "db"), user="root",
                                   password=os.getenv("DB_PASS", "root123"))


def init_db():
    for _ in range(30):
        try:
            c = get_conn(); break
        except mysql.connector.Error:
            time.sleep(3)
    else:
        raise SystemExit("DB not reachable")
    cur = c.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS college")
    cur.execute("USE college")
    cur.execute("CREATE TABLE IF NOT EXISTS students(id INT PRIMARY KEY, name VARCHAR(50), course VARCHAR(30))")
    cur.execute("SELECT COUNT(*) FROM students")
    if cur.fetchone()[0] == 0:          # seed 5 records only once
        cur.executemany("INSERT INTO students VALUES (%s,%s,%s)", [
            (1, "Asha", "DCC"), (2, "Ravi", "DCC"), (3, "Meera", "DAC"),
            (4, "Kabir", "DAC"), (5, "Sneha", "DBDA")])
        c.commit()
    c.close()


@app.route("/")
def students():
    c = get_conn(); cur = c.cursor(); cur.execute("SELECT * FROM college.students")
    rows = "".join(f"<tr><td>{i}</td><td>{n}</td><td>{co}</td></tr>" for i, n, co in cur.fetchall())
    c.close()
    return f"<h2>Students from MySQL</h2><table border='1' cellpadding='6'><tr><th>ID</th><th>Name</th><th>Course</th></tr>{rows}</table>"


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
