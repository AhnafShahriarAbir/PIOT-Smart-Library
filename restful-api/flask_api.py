from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json

api = Blueprint("api", __name__)

db = SQLAlchemy()
ma = Marshmallow()


# Declaring the model.
class Book(db.Model):
    __tablename__ = "Book"
    BookID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Title = db.Column(db.Text)
    # Username = db.Column(db.String(256), unique = True)

    def __init__(self, Title, BookID = None):
        self.BookID = BookID
        self.Title = Title

class BookSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, strict = True, **kwargs):
        super().__init__(strict = strict, **kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("BookID", "Title")

bookSchema = BookSchema()
booksSchema = BookSchema(many = True)

# Endpoint to show all people.
@api.route("/book", methods = ["GET"])
def getBooks():
    books = Book.query.all()
    result = booksSchema.dump(books)

    return jsonify(result.data)

# Endpoint to get Book by id.
@api.route("/book/<id>", methods = ["GET"])
def getBook(id):
    book = Book.query.get(id)

    return bookSchema.jsonify(book)

# Endpoint to create new Book.
@api.route("/book", methods = ["POST"])
def addBook():
    title = request.json["Title"]

    newBook = Book(Title = title)

    db.session.add(newBook)
    db.session.commit()

    return bookSchema.jsonify(newBook)

# Endpoint to update Book.
@api.route("/book/<id>", methods = ["PUT"])
def bookUpdate(id):
    book = Book.query.get(id)
    title = request.json["title"]

    book.Title = title

    db.session.commit()

    return bookSchema.jsonify(book)

# Endpoint to delete Book.
@api.route("/book/<id>", methods = ["DELETE"])
def BookDelete(id):
    book = Book.query.get(id)

    db.session.delete(book)
    db.session.commit()

    return bookSchema.jsonify(book)
