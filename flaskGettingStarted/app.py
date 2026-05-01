from  flask import Flask, render_template,abort
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

@app.route("/card/<int:index>")
def flash_card(index):
    
    try:
        card = db[index]
        return render_template("card.html",
                           card = card,
                           index = index )
    except IndexError:
        abort(404)
    