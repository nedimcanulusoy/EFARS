import os
from io import StringIO

from flask import render_template, request, flash, url_for, send_file, jsonify
from werkzeug.utils import secure_filename, redirect

from efars import app
from efars.utils import allowed_file, allowed_filesize, filesize, pdf_merge, get_absolute_file_path
from efars.visualization import VisualizeData


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']

    if file.filename == "":
        flash('No file part')
        return redirect(url_for('index'))

    if file.filename != "" and allowed_file(file.filename):
        filename_ = secure_filename(file.filename)
        file_path = file.stream.read().decode('utf-8')
        file = StringIO(file_path)

        v = VisualizeData(file)
        v.average_table()
        v.scatter_graph()
        v.bar_graph()
        v.dma_bar_graph()
        v.heatmap_graph()

        pdf_merge()

        flash('File uploaded')
        return redirect(url_for('index'))

    elif not allowed_file(file.filename):
        flash('File type error')
        return redirect(url_for('index'))

    elif allowed_filesize(filesize()) is False:
        flash('File size error')
        return redirect(url_for('index'))

    return render_template('upload.html')


@app.route('/result/<filename>', methods=['GET'])
def display_result(filename):
    file_path = os.getcwd() + "/" + get_absolute_file_path(filename)

    if not os.path.exists(file_path):
        return "ERROR"

    return send_file(file_path)


@app.route('/about/', methods=['GET'])
def about():
    return render_template("about.html")


@app.route('/terms-and-conditions/', methods=['GET'])
def terms_conditions():
    return render_template("terms.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(413)
def file_size_exceed(e):
    return render_template('404.html'), 413
