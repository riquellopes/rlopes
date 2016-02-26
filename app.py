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
    links = [
        ("GitHub", "http://github.com/riquellopes"),
        ("Twitter", "http://twitter.com/riquellopes"),
        ("Linkedin", "https://www.linkedin.com/in/riquellopes"),
        ("Delicious", "https://delicious.com/riquellopes"),
    ]
    return render_template("boot-template.html", links=links)
