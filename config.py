import os

import yaml


class Config(object):
    stream = open(os.getcwd() + "/config.yml", 'r')
    config = yaml.load(stream, Loader=yaml.FullLoader)

    DEBUG = False
    TESTING = False

    SECRET_KEY = config["secret_key"]

    ALLOWED_EXTENSIONS = ["csv"]
    MAX_CONTENT_LENGTH = 2 * 1000 * 1000  # File size limit is 16MB
    DEFAULT_PATH = config['default_folder_path']
    PLOT_PATH = config['plot_folder_path']
    RESULT_PATH = config['result_folder_path']

class DevelopmentConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    DEBUG = False
