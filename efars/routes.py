from efars import app
from flask import Flask, render_template, redirect, url_for, request, make_response

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():

    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print(uploaded_file.filename)
        return {
            'result':"OK"
        },200
        # return make_response(jsonify(result='OK'), 200) # Possible to return with make_response
    else:
        return {
            'result':"ERROR"
        },404

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