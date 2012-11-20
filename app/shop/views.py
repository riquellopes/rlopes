# coding: utf-8
from flask import render_template, Module
from app import db
from app.shop.documents import Iten
from decorators import transaction

store = Module(__name__, 'shop')

@store.route("/")
def home():
	"""
		Method request riquellopes's shop::
	"""
	#itens = Iten.objects.all()
	return render_template('shop/shop_list.html', **locals())

@store.route("/<int:iten>/buy")
def buy(iten):
	"""
		Method redirect user to gateway of payment::
	"""
	pass

@store.route("/<int:iten>/bid")
@transaction
def bid(iten):
	""" 
		Method send a propost for my iten on shop::
	"""
	pass

@store.route("/returns")
def return_gateway():
	"""
		Method get return gateway::
	"""
	pass