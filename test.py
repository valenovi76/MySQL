from flask import Flask
app = Flask(__name__)

@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
def users():