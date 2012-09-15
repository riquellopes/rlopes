# coding: utf-8
from flask import render_template
from flask_mail import Mail, Message, BadHeaderError
from app.shop.documents import Iten
from app import app

mail = Mail(app)

class MakeBid(object):
	""""Container MakeBid::"""
	
	def __init__(self, **kwargs):
		for k in kwargs:
			setattr(self, k, kwargs[k])

	@property
	def iten(self):
		return self._iten

	@iten.setter
	def iten(self, id):
		self._iten = Iten.query.filter({'mongo_id':id}).first()

	@property
	def html_msg(self):
		""" Method create template email Bid::"""
		iten=self.iten
		bid=self.bid
		name=self.name
		text=self.text
		return render_template('shop/email_make_bind.html', **locals())

	def send(self):
		"""Method send a message::"""
		msg = Message(
				subject='Rlopes|shop - Proposta pelo iten %(iten)s' % {'iten':self.iten.name},
				html=self.html_msg,
				sender=self.sender,
				recipients=[app.config.get('MAIL'),]
			)
		try:
			mail.send(msg)
		except BadHeaderError:
			return False
		return True