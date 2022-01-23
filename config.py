import yaml, os


class Config(object):
    stream = open(os.getcwd() + "/config.yml", 'r')
    config = yaml.load(stream, Loader=yaml.FullLoader)

    DEBUG = False
    TESTING = False

    SECRET_KEY = config["secret_key"]

    DB_NAME = config["db"]
    DB_USERNAME = config["user"]
    DB_PASSWORD = config["password"]
    # SQLALCHEMY_DATABASE_URI

    ALLOWED_EXTENSIONS = ["docx"]


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = Config.config["development"]["db"]
    DB_USERNAME = Config.config["development"]["user"]
    DB_PASSWORD = Config.config["development"]["password"]
    # SQLALCHEMY_DATABASE_URI


class ProductConfig(Config):
    DEBUG = False

    DB_NAME = Config.config["production"]["db"]
    DB_USERNAME = Config.config["production"]["user"]
    DB_PASSWORD = Config.config["production"]["password"]
    # SQLALCHEMY_DATABASE_URI


class TestingConfig(Config):
    pass


# TODO Upgrade to Instance folder type in the future
"""
Documentation: http://exploreflask.com/en/latest/configuration.html
Documentation: https://pythonise.com/series/learning-flask/flask-configuration-files
"""
