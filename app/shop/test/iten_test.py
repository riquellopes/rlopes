# coding: utf-8
import unittest
from nose.tools import assert_true, assert_equals, assert_raises, assert_false
from app.shop.documents import Iten, ItenException
from mock import patch

class BaseTestCase(unittest.TestCase):

	def tearDown(self):
		itens = Iten.query.all()
		for iten in itens:
			iten.remove()

class ItenTest(BaseTestCase):
	
	def test_class_iten_exist(self):
		"""Class iten exist::"""
		assert_true(isinstance(Iten, object))

	def test_method_save_should_be_create_a_new_document(self):
		"""Method save should be create a new document::"""
		iten = Iten(name='Placa de som', descriptions='A melhor placa do mercado', price=50.00, url_imagen='')
		iten.save()
		assert_equals(iten.query.count(), 1)

	def test_name_shouldnt_be_empty(self):
		"""Name shouldn't be empty::"""
		iten = Iten(name='', descriptions='A melhor placa do mercado', price=50.00, url_imagen='')
		assert_raises(iten.save)

	def test_method_open_shop_return_true_case_exist_one_or_more_iten_sell(self):
		"""Method open_shop reuturn True case exist one or more iten then sell::"""
		iten = Iten(name='', descriptions='A melhor placa do mercado', price=50.00, url_imagen='')
		iten.save()
		assert_true(Iten.query.open_shop)

	def test_method_open_shop_return_false(self):
		"""Method open_shop return False case no exist itens then sell::"""
		assert_false(Iten.query.open_shop)

class RequestAndSaveInten(BaseTestCase):

	def test_csv_to_iten_and_save_return_true(self):
		"""Csv to iten and save return true::"""
		assert_true(Iten.csv_to_iten('itens.csv'))
		assert_equals(Iten.query.count(), 1)

	def test_case_have_error_system_up_exception(self):
		"""Case have error system up exception::"""
		assert_raises(ItenException, Iten.csv_to_iten, '')
	
	@patch('app.shop.documents.urllib2.urlopen')
	def test_csv_on_web_to_iten_and_save_return_true(self, url):
		"""Csv on web to iten and save return true::"""
		url.return_value = open('itens_2.csv')
		assert_true(Iten.csv_to_iten('http://dl.dropbox.com/u/85377659/itens.csv'))
		assert_equals(Iten.query.count(), 2)