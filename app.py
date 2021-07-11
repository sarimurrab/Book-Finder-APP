# importing required modules
import os
from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from wtforms.fields.core import FormField
from views import Books


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
    return render_template("index.html")


@app.route('/add-book', methods =['POST','GET'])
def add_book():
    form = Books()
    if request.method == 'POST':
        book=BooksModel(request.form['title'].capitalize(), request.form['author'].capitalize(), request.form['published_on'])
        db.session.add(book)
        db.session.commit()
        return render_template('after_add_book.html')
    return render_template('add_book.html', form=form)



@app.route('/search-book', methods =['POST','GET'])
def search_book():
    form = Books()
    bookList = BooksModel.query.order_by(BooksModel.title).all()
    authorList = BooksModel.query.order_by(BooksModel.author).all()
    show = False
    result =  None
    if request.method == 'POST':
        show = True
        result = None
        result = BooksModel.query.filter_by(title=request.form['title']).first()
        print(result)
        if result == None:
            result = BooksModel.query.filter_by(author=request.form['authors']).first()
        
    return render_template('search_book.html', form=form, bookList = bookList, authorList=authorList,result=result, show=show)

@app.route('/list-of-all')
def list_of_all():
    bookList = BooksModel.query.order_by(BooksModel.title).all()
    return render_template('list_of_all.html', bookList=bookList)


@app.route('/delete/<title>')
def delete(title):
    book = BooksModel.query.filter_by(title= title).first()
    db.session.delete(book)
    db.session.commit()
    bookList = BooksModel.query.order_by(BooksModel.title).all()
    return render_template('list_of_all.html', bookList=bookList)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)