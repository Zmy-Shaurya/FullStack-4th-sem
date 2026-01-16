from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> \
    <p>Welcome to the Flask application.</p>"

@app.route("/about/")
def about():
    return "<p>Hello, about page!</p> \
    <p>Welcome to the about page.</p>"

@app.route("/index/")
def index():
    return render_template("index.html")