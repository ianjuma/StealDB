#!/usr/bin/env python
# -*- coding: utf-8 -


from flask import Flask
from flask import render_template
from flask import redirect
from flask import session


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
        return jsonify({'Not Found': 404})


@cache.cached(timeout=50)
@app.route('/WhatsApp/')
def index():
    return render_template('bootstrap.html')


if __name__ == '__main__':
    import newrelic.agent
    newrelic.agent.initialize('newrelic.ini')
    app.run(port=8000, debug=True, host='0.0.0.0')
    # This can be omitted if using gevent wrapped around gunicorn
