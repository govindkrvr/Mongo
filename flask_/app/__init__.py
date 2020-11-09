from flask import Flask
from flask_mongoalchemy import MongoAlchemy
import config


application = Flask(__name__)

application.config['SECRET_KEY'] = "random_string"
application.config['MONGOALCHEMY_SERVER'] = config.configDB['IP']
application.config['MONGOALCHEMY_PORT'] = config.configDB['PORT']
application.config['MONGOALCHEMY_DATABASE'] = config.configDB['DATABASE']
db = MongoAlchemy(application)

from app import views

