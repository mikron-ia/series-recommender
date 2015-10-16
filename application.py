from flask import Flask
from flask import render_template

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/')
def list_recommendations():    
    return render_template('list.html', title='Recommender system')

if __name__ == '__main__':    
    handler = RotatingFileHandler('error.log', maxBytes=20000, backupCount=2)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
