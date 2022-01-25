import config

def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext in config.Config.ALLOWED_EXTENSIONS:
        return True
    else:
        return False

