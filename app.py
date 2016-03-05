from flask import Flask, render_template
from flask_frozen import Freezer
from flask.ext.cache import Cache
from gcontent import get_content

app = Flask(__name__)
app.config.from_object("config")
freezer = Freezer(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route("/")
@cache.cached(timeout=1800)
def home():
    """
        Get first page.
    """
    return render_template("boot-template.html", data=get_content())
