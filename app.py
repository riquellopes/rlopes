# coding: utf-8
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_object("config")
freezer = Freezer(app)


@app.route("/")
def home():
    """
        Get first page.
    """
    links = (
        {'label': 'Git Hub', 'src': 'git.png', 'url': 'http://github.com/riquellopes'},
        {'label': 'Facebook', 'src': 'fb.png', 'url': 'http://fb.com/riquellopes'},
        {'label': 'Twitter', 'src': 'tw.png', 'url': 'http://twitter.com/riquellopes'},
        {'label': 'Linkedin', 'src': 'lin.png', 'url': 'https://www.linkedin.com/in/riquellopes'},
    )
    return render_template("home.html", links=links)
