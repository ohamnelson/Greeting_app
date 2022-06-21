from flask import Flask, flash ,render_template, request


app = Flask(__name__)
app.secret_key = "hello"


@app.route("/hello")
def index():
    flash("What's your Name?")
    return render_template("index.html")

@app.route("/greet", methods = ["POST", "GET"])
def greet():
    request.form["name_input"]
    flash("Hi " + str(request.form["name_input"]) + ", great to see you")
    return render_template("index.html")

    # fetching the input collected from the user



