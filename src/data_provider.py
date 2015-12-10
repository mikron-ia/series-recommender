import sqlite3
import os.path

from flask import Flask
from flask import g

db_path = os.path.join(os.path.dirname(__file__), '../data/recommendations.db')
app = Flask(__name__)

def create_connection():
    return sqlite3.connect(db_path)

def connect():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = create_connection()        
        db.row_factory = make_dictionaries
    return db

@app.teardown_appcontext
def disconnect(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
def make_dictionaries(cursor, row):
    return dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row))

def execute_command(sql):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True

