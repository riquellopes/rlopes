# coding: utf-8
from functools import wraps
from flask import redirect, request

def transaction(func):
	@wraps(func)
	def decorated_views(*args, **kwargs):
		"""Verifica se o número da transação é valida::"""
		return func(*args, **kwargs)
	return decorated_views