
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ntktgepbrb-rjhvbkmws-1963'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://mysql/1?decode_responses=True&health_check_interval=2'
    PROD_APP_NAME = os.environ.get('PROD_APP_NAME') or 'ibcntr'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONF_IMAGES = {
      "uat": "uat.png",
      "bnu": "upp.png",
      "zup": "zup.png"
      }