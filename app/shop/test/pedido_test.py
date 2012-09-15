# coding: utf-8
import unittest
from nose.tools import assert_true, assert_equals, assert_false, assert_not_equals
from app.shop.documents import Iten, Pedido, TRANSACTION_STATUS

class BaseTestCase(unittest.TestCase):
	
	def tearDown(self):
		for p in Pedido.query.all():
			p.remove()

		for i in Iten.query.all():
			i.remove()

class PedidoTest(BaseTestCase):

	def test_pedido_exist(self):
		"""Pedido exist::"""
		assert_true(isinstance(Pedido, object))

	def test_create_one_pedido(self):
		"""Create a pedido::"""
		iten = Iten(name='Placa de som', descriptions='A melhor placa do mercado', price=150.00, url_imagen='')
		iten.save()
		ped = Pedido(email_customer='riquellopes@gmail.com', iten=iten, price_combined=50.00)
		ped.save()
		assert_not_equals(ped.price_combined, iten.price)
		assert_equals(ped.query.count(), 1)

	def test_case_price_combined_empty_the_price_combined_should_be_the_price_iten(self):
		""" Case price empty the price combined should be the price iten::"""
		iten = Iten(name='Placa de som', descriptions='A melhor placa do mercado', price=50.00, url_imagen='')
		iten.save()
		ped = Pedido(email_customer='riquellopes@gmail.com', iten=iten)
		ped.save()
		assert_equals(ped.price_combined, iten.price)
		assert_equals(ped.query.count(), 1)

	def test_process_return_gateway(self):
		"""Process return gateway::"""
		iten = Iten(name='Placa de som', descriptions='A melhor placa do mercado', price=50.00, url_imagen='')
		iten.save()
		ped = Pedido(email_customer='riquellopes@gmail.com', iten=iten)
		ped.save()
		id = ped.mongo_id

		del ped, iten
		assert_true(Pedido.query.paymentProcessing(id, status=3))
		ped = Pedido.query.filter({'mongo_id':id}).first()
		assert_equals(ped.transaction_status, 3)
		assert_equals(ped.transaction_status_str, TRANSACTION_STATUS[3][1])
		assert_true(ped.iten.sold)