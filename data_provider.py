import sqlite3
from flask import g

db_path = '/database/recommendations.db'

def connect():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def disconnect(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
def get_list_of_recommendations():
    sql = 'SELECT title, description, season_count, episodes_per_season, episode_length, trailer, person, associated_links FROM recommendations'
    return connect().execute(sql)
