from flask import Flask

app = Flask(__name__)

if app.config['ENV'] == "production":
    app.config.from_object("config.ProductConfig")
# TODO elif statement can be added later
else:
    app.config.from_object("config.DevelopmentConfig")

from efars import routes