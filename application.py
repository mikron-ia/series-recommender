from flask import Flask
from flask import render_template

import logging
from logging.handlers import RotatingFileHandler

import data_provider

__author__ = "Mikron"

app = Flask(__name__)

@app.route('/')
def list_recommendations():
    list = data_provider.get_list_of_recommendations()    
    return render_template('list.html', title='Recommender system', header='Recommender system', recommendations=list)

@app.route('/add')
def add_recomendation():
    return render_template('add.html', title='Recommender system - add recommendation', header='Recommender system - add recommendation')

@app.route('/add_action')
def add_recommendation_action():
    return None

if __name__ == '__main__':    
    handler = RotatingFileHandler('logs/error.log', maxBytes=20000, backupCount=2)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
