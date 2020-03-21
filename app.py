import os
from os import path
if path.exists("env.py"):
    import env
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME" ,'mongodb://localhost') 

mongo = PyMongo(app)


@app.route('/')


@app.route('/get_requests')
def get_requests():
   return render_template("requests.html", requests=mongo.db.c_requests.find())


# @app.route('/new_requests')
# def add_new_requests():
#     return render_template("new_requests.html", foods=mongo.db.c_food.find())


# @app.route('/insert_requests', methods=['POST'])
# def insert_requests():
 #    requests = mongo.db.c_requests
  #   requests.insert_one(request.form.to_dict())
   #  return redirect(url_for('get_requests'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)