from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv



app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


# miksi seuraava error: 
# RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set.