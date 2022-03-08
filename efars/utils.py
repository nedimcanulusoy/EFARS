from PyPDF2 import PdfFileMerger
from flask import request

import config
import datetime
import glob
import os


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


def folder_exists():
    default_path = config.Config.DEFAULT_PATH
    is_exists = os.path.exists(default_path)

    if not is_exists:
        os.mkdir(default_path)


def generate_filename():
    basename = 'plot'
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S_%f")
    ext = '.'.join([timestamp, 'pdf'])

    return '_'.join([basename, ext])


def create_plot_name():
    return ''.join([config.Config.DEFAULT_PATH, generate_filename()])


def pdf_merge():
    pdf_list = [file for file in glob.glob(config.Config.DEFAULT_PATH + "*.pdf")]
    pdf_list.sort()

    merger = PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(config.Config.DEFAULT_PATH + "result.pdf")
    merger.close()
