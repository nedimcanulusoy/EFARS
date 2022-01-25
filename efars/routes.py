import config
from efars import app
from flask import Flask, render_template, redirect, url_for, request, make_response
from werkzeug.utils import secure_filename
from efars.utils import allowed_file, allowed_filesize, filesize


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        print(f"FILE: {uploaded_file.filename}")

        if allowed_file(filename) and allowed_filesize(filesize()):
            return {
                       'result': "OK"
                   }, 200
        # return make_response(jsonify(result='OK'), 200) # Possible to return with make_response
        elif allowed_file(filename) and not allowed_filesize(filesize()):
            return {
                       'result': "SIZE ERROR"
                   }, 413

        else:
            return {
                       'result': "FILE TYPE ERROR"
                   }, 404
    else:
        return {
                   'result': "ERROR"
               }, 404


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
