import os
from io import StringIO

from flask import render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename

from efars import app
from efars.utils import allowed_file, pdf_merge, get_absolute_file_path
from efars.visualization import VisualizeData


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file.filename != "" and allowed_file(file.filename):
        filename_ = secure_filename(file.filename)
        file_path = file.stream.read().decode('utf-8')
        file = StringIO(file_path)

        v = VisualizeData(file)
        v.average_table()
        v.scatter_graph()
        v.histogram_graph()
        v.dma_bar_graph()
        v.heatmap_graph()

        pdf_filename = pdf_merge()

        return jsonify({"file": pdf_filename})

    return render_template('upload.html')


@app.route('/result/<filename>', methods=['GET'])
def display_result(filename):
    file_path = os.getcwd() + "/" + get_absolute_file_path(filename)

    if not os.path.exists(file_path):
        return render_template('404.html'), 404

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

