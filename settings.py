# coding: utf-8
from os import path, environ

TEST = False
MAIL_CODE = '&#099;&#111;&#110;&#116;&#097;&#116;&#111;&#064;&#104;&#101;&#110;&#114;&#105;&#113;&#117;&#101;&#108;&#111;&#112;&#101;&#115;&#046;&#099;&#111;&#109;&#046;&#098;&#114;' 

try:
	from local_settings import *
except ImportError:
	CONSUMER_SECRET=environ.get('CONSUMER_SECRET')
	CONSUMER_KEY=environ.get('CONSUMER_KEY')