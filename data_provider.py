import sqlite3
from flask import Flask
from flask import g

db_path = 'data/recommendations.db'
app = Flask(__name__)

def create_connection():
    return sqlite3.connect(db_path)

def connect():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = create_connection()
    return db

@app.teardown_appcontext
def disconnect(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
def get_list_of_recommendations():
    sql = 'SELECT title, description, season_count, episodes_per_season, episode_length, trailer, person, associated_links FROM recommendation'
    return connect().execute(sql)
