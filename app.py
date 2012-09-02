# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("settings")

@app.route("/")
def home():
	"""
		Method request the first page of website::
	"""
	links = (
		{'label':'Git Hub', 'src':'git.png', 'url':'http://github.com/riquellopes'},
		{'label':'Facebook', 'src':'fb.png', 'url':'http://fb.com/riquellopes'},
		{'label':'Twitter', 'src':'tw.png', 'url':'http://twitter.com/riquellopes'},
		#{'label':'Linkedin', 'src':'lin.png', 'url':'javascript:;'},
		{'label':'Shop', 'src':'lin.png', 'url':'javascript:;'},
	)
	return render_template("home.html", **locals())

@app.route("/shop")
def shop():
	"""
		Method request riquellopes's shop::
	"""
	pass

@app.route("/shop/<iten:int>")
def iten(id):
	"""
		Method select iten on shop::
	"""
	pass

@app.route("/shop/<iten:int>/buy")
def buy():
	"""
		Method redirect user to gateway of payment::
	"""
	pass

@app.route("/shop/return")
def return_():
	"""
		Method get return payment::
	"""
	pass