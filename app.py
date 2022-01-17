from flask import Flask, render_template, flash, request

app = Flask(__name__)


@app.route("/hello")
def index():
    flash("What's You Name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")
