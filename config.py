# coding: utf-8
# Flask config for Rlopes Project.
from os import path, environ

DEBUG = False

#SITE SETTINGS::
TITLE='Henrique Lopes'

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
META_ROBOTS='index, follow'
META_GOOGLE_SITE_VERIFICATION=environ.get('GOOGLE_SITE_VERIFICATION')


MAIL='contato@henriquelopes.com.br'
MAIL_CODE='&#099;&#111;&#110;&#116;&#097;&#116;&#111;&#064;&#104;&#101;&#110;&#114;&#105;&#113;&#117;&#101;&#108;&#111;&#112;&#101;&#115;&#046;&#099;&#111;&#109;&#046;&#098;&#114;' 


CONSUMER_SECRET=environ.get('CONSUMER_SECRET')
CONSUMER_KEY=environ.get('CONSUMER_KEY')

#GOOGLE ANALITICS SETTINGS::
GA_USE=True
GA_SET_COUNT=environ.get('GA_SET_COUNT')


#MONGODB SETTINGS::
#MONGODB_DB=environ.get('DB_NAME')
#MONGODB_USERNAME=environ.get('DB_USER')
#MONGODB_PASSWORD=environ.get('DB_PASS')
#MONGODB_HOST=environ.get('DB_HOST')
#MONGODB_PORT=environ.get('DB_PORT')

#MAIL SETTINGS::
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_SSL=False
MAIL_DEBUG=False
MAIL_USERNAME=MAIL
MAIL_PASSWORD=environ.get('MAIL_PASSWORD')
DEFAULT_MAIL_SENDER=MAIL

try:
	from local_settings import *
except ImportError:
	pass