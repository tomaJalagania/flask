from  flask import Flask, render_template
from datetime import datetime
from model import db
app = Flask(__name__)

card = db
# create main router
@app.route("/")
def welcome():
    return render_template("welcome.html",
                           messages = "this is message"
                           )

@app.route("/card")
def flash_card():
    return render_template("card.html",
                           card = db[0]
                           )