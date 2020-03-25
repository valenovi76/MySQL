import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env



app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME",
                                            'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')


@app.route('/get_requests')
def get_requests():
    return render_template("requests.html",
                           requests=mongo.db.c_requests.find())


@app.route('/index.html')
def index():
    return render_template("index.html", memebers=mongo.db.c_members.find())


@app.route('/new_requests')
def add_new_requests():
    return render_template("new_requests2.html", foods=mongo.db.c_food.find())


def get_user():
    users = mongo.db.c_users
    users.find()

@app.route('/insert_requests', methods=['POST'])
def insert_requests():
    requests = mongo.db.c_requests
    requests.insert_one(request.form.to_dict())
    return redirect(url_for('add_new_requests'))


@app.route('/insert_login', methods=['POST'])
def insert_login():
    logins = mongo.db.c_user
    logins.insert_one(request.form.to_dict())
    return redirect(url_for('add_new_requests'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)