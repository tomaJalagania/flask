from  flask import Flask, render_template,abort
from datetime import datetime
from model import db
app = Flask(__name__)

card = db
# create main router
@app.route("/")
def welcome():
    cards = db
    return render_template("welcome.html",
                           messages = "this is message",
                           cards = cards
                           )

@app.route("/card/<int:index>")
def flash_card(index):
    
    try:
        card = db[index]
        max_lengt = len(db)
        print(max_lengt)
        return render_template("card.html",
                           card = card,
                           index = index,
                           max_lengt = max_lengt - 1
                             )
    except IndexError:
        abort(404)
    
