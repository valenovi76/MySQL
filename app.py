import os
from os import path
if path.exists("env.py"):
    import env
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


# Python3 code to display hostname and 
# IP address 
  
# Importing socket library 
import socket 
  
# Function to display hostname and 
# IP address 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
  
# Driver code 
get_Host_name_IP() #Function call 
  
#This code is conributed by "Sharad_Bhardwaj". 




app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME" ,'mongodb://localhost') 

mongo = PyMongo(app)


@app.route('/')


@app.route('/get_requests')
def get_requests():
    return render_template("requests.html", requests=mongo.db.c_requests.find())


@app.route('/new_requests')
def add_new_requests():
    return render_template("new_requests.html", foods=mongo.db.c_food.find())


@app.route('/my_requests')
def get_requests():
    return render_template("my_requests.html", requests=mongo.db.c_requests.find(host_name))   


@app.route('/udate_requests')
def get_requests():
    return render_template("update_requests.html", requests=mongo.db.c_requests.find(host_name))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)