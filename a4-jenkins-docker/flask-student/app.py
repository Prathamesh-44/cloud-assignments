from flask import Flask

app = Flask(__name__)

STUDENT = {"Name": "Your Name", "Roll No": "101", "Course": "PG-DCC", "Centre": "C-DAC Pune"}


@app.route("/")
def home():
    rows = "".join(f"<tr><td><b>{k}</b></td><td>{v}</td></tr>" for k, v in STUDENT.items())
    return f"<h2>Student Details</h2><table border='1' cellpadding='6'>{rows}</table>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
