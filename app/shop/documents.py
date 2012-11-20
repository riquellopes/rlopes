# coding: utf-8
import os
import datetime
import csv
import re
import urllib2
from flask_mongoengine import QuerySet, ValidationError
from mongoengine import signals
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

class MakeABidQuerySet(QuerySet):

	def my_bids(self, hash_transaction=None):
		"""Request my bids::"""
		return self.filter(hash_transaction__startswith=str(hash_transaction)[0:8])

class MakeABid(db.Document):
	"""Container of bids::"""
	meta = {'queryset_class': MakeABidQuerySet}
	hash_transaction=db.StringField(primary_key=True)
	bid=db.FloatField()
	customer_email=db.EmailField()
	date_bid=db.DateTimeField(default=now())
	iten=db.ReferenceField('Iten', dbref=False)

		
	@classmethod
	def pre_save(cls, sender, document, **kwargs):
		"""The method pre_save should be create a hash_transaction."""
		def _hash():
			transactions = cls.objects.filter( hash_transaction__startswith=str(document.hash_transaction)[0:8]).count()
			if transactions:
				return '%s#%s' % ( str(document.hash_transaction)[0:8], transactions + 1 ) 
			return '%s#%s' % (os.urandom(4).encode('hex'), 1)

		document.hash_transaction = _hash()

	@classmethod
	def post_save(cls, sender, document, **kwargs):
		"""
			After save bid, a email should be sender to the Cliente or User::

			1 - Quando o usuário der um lace, o sistema deve verificar o iten foi configurado para
			parar dar um contra lance de resposta automativo. Caso esteje o sistema deve verificar
			se o lance dado está de acordo com o valor que cliente deseja. Caso esja o usuario já 
			deve receber uma mensagem na tela informando que o ele pode comprar o produto. 
			O cliente do serviço é avisado e os 2 entram em um acordo para que o usuário faça o pagamento do
			iten. O sistema deve permitir apenas lances de uma região que o cliente desejar. O cep é deve ser
			informado quando um usuário for fazer um lance.
		"""
		pass

signals.pre_save.connect(MakeABid.pre_save, sender=MakeABid)
signals.post_save.connect(MakeABid.post_save, sender=MakeABid)

class ItenException(Exception):
	pass

class ItenQuerySet(QuerySet):

	@property
	def open_shop(self):
		"""Method verific if shop should open::"""
		return bool(True if self.filter({'sell':True}).count() else False)

class Iten(db.Document):
	"""Container Iten::"""
	meta = {'queryset_class': ItenQuerySet}
	name=db.StringField()
	salesman=db.EmailField()
	descriptions=db.StringField(required=False)
	date_created=db.DateTimeField(default=now())
	price=db.FloatField(required=False, default=0.00)
	sold=db.BooleanField(default=False)
	sell=db.BooleanField(default=True)
	url_imagen=db.StringField(required=False)


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

class PedidoQuerySet(QuerySet):

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

		- A Pedido is created only to credcard payments and bids.
	"""
	meta = {'queryset_class': PedidoQuerySet}
	email_customer=db.EmailField()
	iten=db.ReferenceField(Iten, dbref=False)
	price_combined=db.FloatField(required=True)
	price_ship=db.FloatField(required=False, default=0.00)
	zip_code_customer=db.StringField(required=False)
	transaction_status=db.IntField(default=0)
	date_created=db.DateTimeField(default=now())
	date_process=db.DateTimeField(required=False)


	def save(self, safe=None):
		if self.price_combined is None:
		   self.price_combined = self.iten.price
		super(Pedido, self).save(safe)

	@property	
	def transaction_status_str(self):
		return TRANSACTION_STATUS[self.transaction_status][1]