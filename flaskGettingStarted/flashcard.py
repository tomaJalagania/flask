from  flask import Flask
from datetime import datetime
app = Flask(__name__)

# create main router
@app.route("/")
def welcome():
    return "Welocm to my flashkard application"

@app.route("/date")
def date():
    return "this server return "+str(datetime.now())