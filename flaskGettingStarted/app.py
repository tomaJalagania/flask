from  flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

# create main router
@app.route("/")
def welcome():
    return render_template("welcome.html")

