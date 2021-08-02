from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
#setup flask app
app = Flask(__name__)
CORS(app)

#Database config
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('POSTGRES_DB')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#import routes/views - important to import it after setting app and relevant db config
import api.views

