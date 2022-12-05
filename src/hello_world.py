from flask import Flask, render_template

from src.database_connection import Database

app = Flask(__name__)
db = Database()

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route("/")
def hello_world():
    # make query before hand here
    games = db.hello_world()
    print(games)
    # pass it into the render_template
    return render_template("home.html", games=games)
