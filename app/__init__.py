from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app: Flask = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db: SQLAlchemy = SQLAlchemy(app)
ma: Marshmallow = Marshmallow(app)

migrate: Migrate = Migrate(app, db)

from app import routes, models


