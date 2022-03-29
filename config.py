import os
import secrets

import yaml


class Config(object):
    config_path = os.getcwd() + "/config.yml"
    file_exists = os.path.exists(config_path)

    if not file_exists:
        data = dict(
            secret=secrets.token_hex(32),

            default_folder_path="efars/process/",
            plot_folder_path="plots/",
            result_folder_path="result/",
        )

        with open(config_path, 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)

    stream = open(config_path, 'r')
    config = yaml.load(stream, Loader=yaml.FullLoader)

    DEBUG = False
    TESTING = False

    SECRET_KEY = config['secret']

    ALLOWED_EXTENSIONS = ["csv"]
    MAX_CONTENT_LENGTH = 2 * 1000 * 1000
    DEFAULT_PATH = config['default_folder_path']
    PLOT_PATH = config['plot_folder_path']
    RESULT_PATH = config['result_folder_path']

class DevelopmentConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    DEBUG = False
