from efars import app
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template("index.html")
