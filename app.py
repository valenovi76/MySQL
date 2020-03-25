import os
import socket
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env



app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME" ,'mongodb://localhost') 
app.secret_key = "randomstring123"
messages = []


mongo = PyMongo(app)

@app.route('/get_requests')
def get_requests():
    return render_template("requests.html", requests=mongo.db.c_requests.find())

# Function to display foodtable from db
@app.route('/new_requests')
def add_new_requests():
    return render_template("new_requests.html", foods=mongo.db.c_food.find())


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


def get_hostname():
    hostname = socket.gethostname()
    return hostname

#@app.route('/my_requests')
#def my_requests():
#return render_template("my_requests.html", requests=mongo.db.c_requests.find(hostname))   


#@app.route('/udate_requests')
#def update_requests():
#return render_template("update_requests.html", requests=mongo.db.c_requests.find(host_name))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)