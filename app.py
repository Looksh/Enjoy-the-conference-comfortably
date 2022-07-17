from tistory import extract_conference_title, extract_conference_content
from flask import Flask, render_template

app = Flask("enjoy-the-conference-comfortably")

@app.route("/")
def home():
    return render_template("home.html")

app.run(debug = True)

