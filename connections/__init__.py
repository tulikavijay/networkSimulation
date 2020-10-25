import os
import markdown

import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    '''
    README.md contents open up
    '''
    with open(os.path.dirname(app.root_path) + 'README.md', 'r') as markdown_file:
            content = markdown_file.read()
            return markdown.markdown(content)
