#!/usr/bin/env python
# -*- coding: utf-8 -

import os

from flask import Flask
from flask import render_template, request
from flask import redirect
from flask import url_for
from flask import session, jsonify, json
from werkzeug.utils import secure_filename

from flask import make_response
from flask import abort

UPLOAD_FOLDER = '/root/DB'
ALLOWED_EXTENSIONS = set(['.db', '.crypt'])


app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/api/v1/WhatsApp/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    response = make_response(jsonify({"OK": "Content Saved"}), 200)
    response.cache_control.no_cache = True
    return response

@app.route("/")
def home():
    return render_template("index.html")


#@app.errorhandler(404)
#def page_not_found(e):
#    return make_response(jsonify({'Error 404':
#                                  "Not Found"}), 404)



# response objects with no cache
@app.route('/api/v1/contact/', methods=['POST', 'GET'])
def getMemById():
    if not request.json:
        abort(400)

    if request.headers['Content-Type'] != 'application/json':
        abort(400)

    if request.method == 'GET':
        pass


    if request.method == 'POST':
        name = request.json.get('name')
        email = request.json.get('email')
        message = request.json.get('message')

        


    resp = make_response(jsonify(db_rep))
    resp.cache_control.no_cache = True
    return resp



@app.errorhandler(404)
def page_not_found(e):
    resp = jsonify({"Error 404": "Not Found"})
    resp.status_code = 404
    return resp


@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({"Error 400":
                                  "Bad request"}), 400)


@app.errorhandler(500)
def internal_error(e):
    return make_response(jsonify({"Error 500":
                                  "Internal Server Error"}), 500)


@app.errorhandler(405)
def invalidMethod(e):
    return make_response(jsonify({"Error 405":
                                  "Invalid Request Method"}), 405)


@app.errorhandler(410)
def gone(e):
    return make_response(jsonify({"Error 410":
                                  "Resource is Gone"}), 410)


if __name__ == '__main__':
    # import newrelic.agent
    # newrelic.agent.initialize('newrelic.ini')
    app.run(port=8000, debug=True, host='0.0.0.0')
    # This can be omitted if using gevent wrapped around gunicorn
