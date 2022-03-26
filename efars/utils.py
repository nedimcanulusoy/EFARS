import datetime
import glob
import os

from PyPDF2 import PdfFileMerger
from flask import request

import config


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
    plot_path = default_path + config.Config.PLOT_PATH
    plot_sub_path = plot_path + datetime.datetime.now().strftime("%y%m%d_%H%M%S_%f")
    result_path = default_path + config.Config.RESULT_PATH

    is_dp_exists = os.path.exists(default_path)
    is_pp_exists = os.path.exists(plot_path)
    is_rp_exists = os.path.exists(result_path)

    if not is_dp_exists and not is_pp_exists and not is_rp_exists:
        os.mkdir(default_path), os.mkdir(plot_path), os.mkdir(result_path)

    if not os.path.exists(plot_sub_path):
        os.mkdir(plot_sub_path)

def generate_filename():
    basename = 'plot'
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S_%f")
    ext = '.'.join([timestamp, 'pdf'])

    return '_'.join([basename, ext])


def create_plot_name():
    newest = max(glob.glob(os.path.join(config.Config.PLOT_PATH, '*/')), key=os.path.getmtime)
    return ''.join([newest, generate_filename()])


def pdf_merge():
    result_sub_path = ''.join([config.Config.RESULT_PATH, datetime.datetime.now().strftime("%y%m%d_%H%M%S_%f")])

    if not os.path.exists(result_sub_path):
        os.mkdir(result_sub_path)

    newest_plot_folder = max(glob.glob(os.path.join(config.Config.PLOT_PATH, '*/')), key=os.path.getmtime)
    newest_result_folder = max(glob.glob(os.path.join(config.Config.RESULT_PATH, '*/')), key=os.path.getmtime)

    pdf_list = [file for file in glob.glob(newest_plot_folder + "*.pdf")]
    pdf_list.sort()

    merger = PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(newest_result_folder + "result.pdf")
    merger.close()


def access_result():
    return max(glob.glob(os.path.join(config.Config.RESULT_PATH, '*/')), key=os.path.getmtime)
