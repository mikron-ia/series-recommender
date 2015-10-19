# Series Recommender
Simple training project written in Python. Its purpose is to provide a platform for recommendations of watched series, good music, and similar media.

## Technologies
* Python with Flask
* SQLite
* HTML5

## Installation guide
1. Install Python - version 2.7 suggested
1. Install `virtualenv` - [detailed instructions for different OSes](https://virtualenv.pypa.io/en/latest/installation.html)
1. Activate `virtualenv`
    * Linux / OS X shell - `venv/bin/activate`
    * Windows cmd - `venv\scripts\activate`
1. Run `pip install -r requirements`
1. Run `python application.py`
1. Open `http://localhost:5000` in browser of choice

## To do
Ideas are presented in order of importance, as perceived:

* Write and test insert form
* Find a way to include CSSes correctly
* Dockerize the installation process
* Create better error handling, especially re: database errors
