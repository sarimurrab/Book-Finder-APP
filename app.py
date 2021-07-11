# importing required modules
import os
from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# initialize the Flask app
app = Flask(__name__)

# database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "mysecret"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# application route
@app.route('/')
def index():
    return "Starter Page"


if __name__ == "__main__":

    app.run(debug=True)