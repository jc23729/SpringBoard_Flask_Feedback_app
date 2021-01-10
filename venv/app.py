from flask import flask, redirect, session

app = Flask(__name__)

@app.route("/")
def homepage():
    """Homepage of site; redirect to register."""

    return redirect("/register")