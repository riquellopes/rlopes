# coding: utf-8
from os import path, environ

TEST=False
TITLE='Henrique Lopes'

##############################
# Meta tags:				 #
##############################
META_DESCRIPTION = (
	'python', 
	'php',
	'developer', 
	'rlopes',
	'riquellopes,'
	'henrique lopes',
	'flask',
	'nosql', 
	'javascript',
)

META_KEYWORDS='Desenvolvedor carioca e apaixonado pelo que faz.'
META_AUTHOR='Henrique Lopes'
META_ROBOTS=(
	'index',
	'follow',
)

META_GOOGLE_SITE_VERIFICATION=environ.get('GOOGLE_SITE_VERIFICATION')

##############################
# Email:				 	 #
##############################
MAIL='contato@henriquelopes.com.br'
MAIL_CODE='&#099;&#111;&#110;&#116;&#097;&#116;&#111;&#064;&#104;&#101;&#110;&#114;&#105;&#113;&#117;&#101;&#108;&#111;&#112;&#101;&#115;&#046;&#099;&#111;&#109;&#046;&#098;&#114;' 

##############################
# Secreat:				 	 #
##############################
CONSUMER_SECRET=environ.get('CONSUMER_SECRET')
CONSUMER_KEY=environ.get('CONSUMER_KEY')

##############################
# Google Analitics:			 #
##############################
GA_USE=True
GA_SET_COUNT=environ.get('GA_SET_COUNT')


try:
	from local_settings import *
except ImportError:
	pass