import config
from flask import request

def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext in config.Config.ALLOWED_EXTENSIONS:
        return True
    else:
        return False

def filesize():
    size_request = request.files['file'].read()
    size = len(size_request)
    return size

def allowed_filesize(filesize):

    if int(filesize) <= config.Config.MAX_CONTENT_LENGTH:
        return True
    else:
        return False