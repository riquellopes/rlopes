from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

db=MongoEngine(app)

@app.errorhandler(404)
def not_found(error):
 	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
	return render_template("500.html", error=error), 500

from app.mysite.views import mysite
from app.shop.views import store

app.register_module(mysite)
app.register_module(store, url_prefix='/shop')