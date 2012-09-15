# coding: utf-8
import unittest
from nose.tools import assert_true, assert_equals, assert_false
from app import app
from app.shop.sends import MakeBid
from app.shop.documents import Iten
from mock import patch

class BaseTestCase(unittest.TestCase):
	
	def tearDown(self):
		for i in Iten.query.all():
			i.remove()

class MakeBidTest(BaseTestCase):
	
	def setUp(self):
		app.config['TESTING'] = True

	@patch('app.shop.sends.mail.send')
	def test_send_bind_for_my_email(self, s):
		"""Method send a email to personal email::"""
		with app.test_request_context():
			iten = Iten(name='Placa de som', descriptions='A melhor placa do mercado', price=50.00, url_imagen='')
			iten.save()
			s.return_value = None
			m = MakeBid(
					sender='contato@henriquelopes.com.br',
					bid=100.00,
					name='Jonas Claro',
					text='Vc ainda está com esse produto?',
					iten=iten.mongo_id
				)
			assert_true(m.send())