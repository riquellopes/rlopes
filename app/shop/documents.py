# coding: utf-8
import datetime
import csv
import urllib2
from flaskext.mongoalchemy import BaseQuery, MongoAlchemy
from app import db

# Date current:
now = datetime.datetime.now

def iopen(file):
	"""
		Method open file::
	"""
	try: 
		return open(file)
	except:
		www = urllib2.urlopen(file)
		return www

class ItenException(Exception):
	pass

class ItenQuery(BaseQuery):

	def open_shop(self):
		"""Method verific if shop should open::"""
		return False

class Iten(db.Document):
	"""Container Iten"""
	query_class = ItenQuery
	name=db.StringField()
	descriptions=db.StringField(required=False)
	date_created=db.DateTimeField(default=now())
	price=db.FloatField(required=False, default=0.00)
	sold=db.BoolField(default=False)
	sell=db.BoolField(default=True)
	url_imagen = db.StringField()

	def __repr__(self):
		return '<%s, %s>' % (self.name, self.price)

	@staticmethod
	def csv_to_iten(path_file=None):
		"""Method parse file Csv to Object Iten::"""
		try:
			itens = csv.reader(iopen(path_file), delimiter=';')
			for[name, descriptions, price, sold, sell, url_imagen] in itens:
				iten = Iten(name=name, descriptions=descriptions, price=float(price), sold=bool(sold), sell=bool(sell), url_imagen=url_imagen)
				iten.save()
		except:
			raise ItenException("Error itens not created.")
		return True