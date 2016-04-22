from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('imagebattle.config')

db = SQLAlchemy(app)

from .import api
from . import hooks
from . import models
from .import views
