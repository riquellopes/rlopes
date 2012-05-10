# coding: utf-8
from os import path, environ

TEST = False
MAIL_CODE = '&#114;&#105;&#113;&#117;&#101;&#108;&#108;&#111;&#112;&#101;&#115;&#064;&#103;&#109;&#097;&#105;&#108;&#046;&#099;&#111;&#109;' 

try:
	from local_settings import *
except ImportError:
	CONSUMER_SECRET=environ.get('CONSUMER_SECRET')
	CONSUMER_KEY=environ.get('CONSUMER_KEY')