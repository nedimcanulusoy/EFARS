from flask import Flask

from efars.utils import clear_conversions

app = Flask(__name__)

if app.config['ENV'] == "production":
    app.config.from_object("config.ProductConfig")
# TODO elif statement can be added later
else:
    app.config.from_object("config.DevelopmentConfig")

clear_conversions()
from efars import routes