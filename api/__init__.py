from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#setup flask app
app = Flask(__name__)
CORS(app)

#Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mxsgzsff:gO5Q-UxwZRNEoupNtVSjnVhywGE506pV@tai.db.elephantsql.com/mxsgzsff"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#import routes/views - important to import it after setting app and relevant db config
import api.views

