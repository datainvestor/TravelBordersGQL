from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
#setup flask app
app = Flask(__name__)
CORS(app)

#Database config
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('POSTGRES_DB')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #disable tracking modification of objects and sending signals to the application for every database change
db = SQLAlchemy(app)
migrate = Migrate(app, db)


"""
import routes/views - important to import it after setting app and relevant db config
place at the bottom of the file (we do not use views here, only ensure its imported)
"""
import api.views

