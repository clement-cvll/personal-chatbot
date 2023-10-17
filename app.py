import flask
from flask import render_template, url_for, request, redirect, flash, session

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # Only for development
    app.run(debug=True)