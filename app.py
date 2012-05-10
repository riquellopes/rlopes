# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("settings")

@app.route("/")
def home():
	"""
		Recupera a primeira página do site::
	"""
	links = (
		{'label':'Git Hub', 'src':'git.png', 'url':'http://github.com/riquellopes'},
		{'label':'Facebook', 'src':'fb.png', 'url':'http://fb.com/riquellopes'},
		{'label':'Twitter', 'src':'tw.png', 'url':'http://twitter.com/riquellopes'},
	)
	return render_template("home.html", **locals())