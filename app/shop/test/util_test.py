# coding: utf-8
import unittest
from nose.tools import assert_true, assert_equals, assert_false
from app.shop.documents import MakeABid, Iten
import re

class BaseTest(unittest.TestCase):

	def setUp(self):
		self.iten = Iten(name='Placa de som', descriptions='A melhor placa do mercado', price=50.00, salesman='contato@henriquelopes.com.br').save()
		for m in MakeABid.objects.all():
			m.delete()

	def tearDown(self):
		self.iten.delete()
		
class UtilTest(BaseTest):

	
	def test_method_save_in_makeABid_should_create_a_hash(self):
		"""Method save in makeABid should be create a hash transaction::"""
		make = MakeABid(bid=100.00, customer_email='riquellopes@gmail.com', iten=self.iten).save()
		assert_true(len(make.hash_transaction))
	
	def test_case_iten_has_make_a_bid_hash_transaction_should_be_2_at_final(self):
		"""Case iten has make a bid final hash_transaction, should be 2::"""
		make_1 = MakeABid(bid=100.00, customer_email='riquellopes@gmail.com', iten=self.iten)
		make_1.save()
		assert_true(len(make_1.hash_transaction))

		make_2 = MakeABid(bid=100.00, customer_email='riquellopes@gmail.com', iten=self.iten, hash_transaction=make_1.hash_transaction)
		make_2.save()
		assert_true(len(make_2.hash_transaction))
		assert_true(re.search('#2', make_2.hash_transaction))

		make_3 = MakeABid(bid=110.00, customer_email='jonas@gmail.com', iten=self.iten)
		make_3.save()
		assert_true(re.search('#1', make_3.hash_transaction))

	def test_bid_against(self):
		"""Simulations process of bids::"""
		make_1 = MakeABid(bid=120.00, customer_email='riquellopes@gmail.com', iten=self.iten)
		make_1.save()
		assert_true(re.search('#1', make_1.hash_transaction))

		make_2 = MakeABid(bid=125.00, customer_email='contato@henriquelopes.com.br', iten=self.iten, hash_transaction=make_1.hash_transaction)
		make_2.save()
		assert_true(re.search('#2', make_2.hash_transaction))

		make_3 = MakeABid(bid=122.00, customer_email='riquellopes@gmail.com', iten=self.iten, hash_transaction=make_2.hash_transaction)
		make_3.save()
		assert_true(re.search('#3', make_3.hash_transaction))


		assert_equals(MakeABid.objects.my_bids( make_3.hash_transaction ).count(), 3)