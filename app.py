#imports#
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

#flask app#
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME",
                                            'mongodb://localhost')

mongo = PyMongo(app)

#routing#
@app.route('/')
#index page#
@app.route('/index')
def index():
    return render_template("index.html",
                           member_types=mongo.db.c_member_type.find())

#new requests page#
@app.route('/new_requests')
def new_requests():
    return render_template("new_requests.html",
                           members=mongo.db.c_members.find(),
                           shops=mongo.db.c_shops.find(),
                           status=mongo.db.c_status.find())

#requests page to filter current requests#
@app.route('/requests')
def requests():
    return render_template("requests.html",
                           requests=mongo.db.c_requests.find())

#add data to mongo db collection requests#
@app.route('/insert_requests', methods=['POST'])
def insert_requests():
    requests = mongo.db.c_requests
    requests .insert_one(request.form.to_dict())
    return redirect(url_for('requests'))

#add data to mongo db collection members#
@app.route('/insert_login', methods=['POST'])
def insert_login():
    usernames = mongo.db.c_members
    usernames.insert_one(request.form.to_dict())
    return redirect(url_for('new_requests'))

# routing to edit page and getting data from mongo db collection requests#
@app.route('/edit_request/<request_id>')
def edit_request(request_id):
    the_request = mongo.db.c_requests.find_one({"_id": ObjectId(request_id)})
    all_members = mongo.db.c_members.find()
    all_shops = mongo.db.c_shops.find()
    all_status = mongo.db.c_status.find()
    return render_template("edit_request.html", request=the_request,
                           members=all_members, shops=all_shops,
                           status=all_status)

# updating data on mongo db collection requests#
@app.route('/update_request/<request_id>', methods=["POST"])
def update_request(request_id):
    requests = mongo.db.c_requests
    requests.update({"_id": ObjectId(request_id)},
                    {'requested_by': request.form.get('requested_by'),
                    'phone': request.form.get('phone'),
                     'shop': request.form.get('shop'),
                     'shopping_date': request.form.get('shopping_date'),
                     'food': request.form.get('food'),
                     'status': request.form.get('status')
                     })
    return redirect(url_for('requests'))

#delete document in request collection on mongo db#
@app.route('/delete_request/<request_id>')
def delete_request(request_id):
    mongo.db.c_requests.remove({'_id': ObjectId(request_id)})
    return redirect(url_for('requests'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
