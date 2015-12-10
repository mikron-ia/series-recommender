from flask import Flask
from flask import request

import logging
from logging.handlers import RotatingFileHandler

import src.controllers.recommendations

__author__ = "Mikron"

app = Flask(__name__)


@app.route('/')
def index():
    recommendations = src.controllers.recommendations.Recommendations()
    return recommendations.index()


@app.route('/index')
def _index():
    recommendations = src.controllers.recommendations.Recommendations()
    return recommendations.index()


@app.route('/new', methods=['GET', 'POST'])
def add_recommendation():
    recommendations = src.controllers.recommendations.Recommendations()
    return recommendations.new(request)

if __name__ == '__main__':    
    handler = RotatingFileHandler('logs/error.log', maxBytes=20000, backupCount=2)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
