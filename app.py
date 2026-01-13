from flask import Flask, render_template
from ai_modules.proctoring_engine import start_proctoring
from ai_modules.violation_tracker import get_report

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/exam")
def exam():
    start_proctoring()
    return render_template("exam.html")

@app.route("/report")
def report():
    data = get_report()
    return render_template("report.html", report=data)

if __name__ == "__main__":
    app.run(debug=True)
