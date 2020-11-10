from flask import Flask
from flask_mongoalchemy import MongoAlchemy
import config


application = Flask(__name__)

application.config['SECRET_KEY'] = "random_string"
#application.config['MONGOALCHEMY_SERVER'] = config.configDB['IP']
#application.config['MONGOALCHEMY_PORT'] = config.configDB['PORT']
application.config['MONGOALCHEMY_DATABASE'] = config.configDB['DATABASE']
application.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://127.0.0.1:27017'
db = MongoAlchemy(application)

from app import views

