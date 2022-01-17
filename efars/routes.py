from efars import app
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about/', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/terms-and-conditions/')
def terms_conditions():
    return render_template("terms.html")