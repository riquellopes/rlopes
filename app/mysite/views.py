# coding: utf-8
from flask import render_template, Module
from app.shop.documents import Iten

mysite = Module(__name__, 'mysite')

@mysite.route("/")
def home():
	"""
		Method request the first page of website::
	"""
	links = (
		{'label':'Git Hub', 'src':'git.png', 'url':'http://github.com/riquellopes', 'target':'_blank'},
		{'label':'Facebook', 'src':'fb.png', 'url':'http://fb.com/riquellopes', 'target':'_blank'},
		{'label':'Twitter', 'src':'tw.png', 'url':'http://twitter.com/riquellopes', 'target':'_blank'},
		{'label':'Linkedin', 'src':'lin.png', 'url':'http://br.linkedin.com/in/riquellopes', 'target':'_blank'},
		{'label':'Shop', 'src':'lin.png', 'url': '/shop' if Iten.objects.open_shop else 'javascript:;' , 'target':'_self'},
	)
	return render_template("mysite/home.html", **locals())