from  flask import Flask

app = Flask(__name__)

# create main router
@app.route("/")
def welcome():
    return "Welocm to my flashkard application"