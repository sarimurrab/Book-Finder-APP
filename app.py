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

# Models
class BooksModel(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date

    def __repr__(self):
        return f"{self.id},{self.title},{self.author},{self.published_date}"


# Application routes
@app.route('/')
def index():
    return "Starter Page"


if __name__ == "__main__":

    app.run(debug=True)