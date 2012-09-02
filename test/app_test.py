# coding: utf-8
import unittest
from nose.tools import assert_true
from app import app

class RlopesTest(unittest.TestCase):
	
	def setUp(self):
		self.app = app.test_client()
	
	def test_a_pagina_index_vai_possuir_o_titulo(self):
		"""
			A página home, deve possuir o titulo XXX | Home::
		"""
		rs = self.app.get("/")
		assert_true("<title>%s | Home</title>" % app.config['TITLE'] in str(rs.data))
		assert_true("Git Hub" in str(rs.data))
		assert_true("Facebook" in str(rs.data))
		assert_true("Twitter" in str(rs.data))
	
	def test_mail_code(self):
		"""
			O email de contato deve esta ofuscado::
		"""
		rs = self.app.get("/")
		assert_true(app.config['MAIL_CODE'] in str(rs.data))

class RlopesShopTest(unittest.TestCase):
	pass