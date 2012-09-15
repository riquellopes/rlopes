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

	@property
	def open_shop(self):
		"""Method verific if shop should open::"""
		return bool(self.filter({'sell':True}).count())

class Iten(db.Document):
	"""Container Iten::"""
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

TRANSACTION_STATUS = (
	(0, 'Liberado Para Pagamento'),
	(1, 'Completo'),
	(2, 'Aguardando Pagamento'),
	(3, 'Aprovado'),
	(4, 'Em Análise'),
	(5, 'Cancelado'),
)

class PedidoQuery(BaseQuery):

	def paymentProcessing(self, id, status):
		""" Method as process return payment::"""
		ped = self.filter({'mongo_id':id}).first()
		ped.transaction_status = status
		ped.date_process = now()
		ped.iten.sold = True
		ped.iten.save()
		ped.save()
		return True

class Pedido(db.Document):
	"""
		Container Pedido::

		- A Pedido is created only to credcard payments.
	"""
	query_class = PedidoQuery
	email_customer=db.StringField()
	iten=db.DocumentField(Iten)
	price_combined=db.FloatField(required=True)
	price_ship=db.FloatField(required=False, default=0.00)
	zip_code_customer=db.StringField(required=False)
	transaction_status=db.IntField(default=0)
	date_created=db.DateTimeField(default=now())
	date_process=db.DateTimeField(required=False)

	def __repr__(self):
		return '<%s, %s>' % (self.email, self.iten.name)

	def save(self, safe=None):
		try:
			self.price_combined
		except AttributeError:
			self.price_combined = self.iten.price
		super(Pedido, self).save(safe)

	@property	
	def transaction_status_str(self):
		return TRANSACTION_STATUS[self.transaction_status][1]