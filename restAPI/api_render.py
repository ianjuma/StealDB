#!/usr/bin/env python
# -*- coding: utf-8 -

import os

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/synod/Desktop/WhatsApp'
ALLOWED_EXTENSIONS = set(['.db', '.crypt'])


app = Flask(__name__)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/api/v0.0.1/WhatsApp/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return jsonify({'OK': 200})

@app.errorhandler(404)
def page_not_found(e):
        return jsonify({'Not Found': 404})


if __name__ == '__main__':
    # import newrelic.agent
    # newrelic.agent.initialize('newrelic.ini')
    app.run(port=8000, debug=True, host='0.0.0.0')
    # This can be omitted if using gevent wrapped around gunicorn
