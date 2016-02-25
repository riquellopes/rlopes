from os import environ

FREEZER_DESTINATION = "output"
TEST = environ.get("TEST", False)
MAIL_CODE = '&#099;&#111;&#110;&#116;&#097;&#116;&#111;&#064;&#104;&#101;&#110;&#114;&#105;&#113;&#117;&#101;&#108;&#111;&#112;&#101;&#115;&#046;&#099;&#111;&#109;&#046;&#098;&#114;'
CONSUMER_KEY = environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
