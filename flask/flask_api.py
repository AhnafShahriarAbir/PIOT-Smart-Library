from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json

api = Blueprint("api", __name__)

db = SQLAlchemy()
ma = Marshmallow()

# Declaring the model.
class User(db.Model):
    __tablename__ = "User"
    UserID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    User_name = db.Column(db.Text)
    # Username = db.Column(db.String(256), unique = True)

    def __init__(self, user_name, UserID = None):
        self.UserID = UserID
        self.user_name = user_name

class UserSchema(ma.Schema):
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, strict = True, **kwargs):
        super().__init__(strict = strict, **kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("UserID", "user_name")

userSchema = UserSchema()
usersSchema = UserSchema(many = True)

# Endpoint to show all people.
@api.route("/user", methods = ["GET"])
def getUser_email():
    user_email = User.query.all()
    result = usersSchema.dump(user_email)

    return jsonify(result.data)

# Endpoint to get person by id.
@api.route("/user/<id>", methods = ["GET"])
def getUser(id):
    user = User.query.get(id)

    return userSchema.jsonify(user)

# Endpoint to create new person.
@api.route("/user", methods = ["POST"])
def addUser():
    user_name = request.json["user_name"]

    newUser = User(user_name = user_name)

    db.session.add(newUser)
    db.session.commit()

    return userSchema.jsonify(newUser)

# Endpoint to update person.
@api.route("/user/<id>", methods = ["PUT"])
def userUpdate(id):
    user = User.query.get(id)
    user_name = request.json["user_name"]

    user.User_name = user_name

    db.session.commit()

    return userSchema.jsonify(user)

# Endpoint to delete person.
@api.route("/user/<id>", methods = ["DELETE"])
def userDelete(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return userSchema.jsonify(user)