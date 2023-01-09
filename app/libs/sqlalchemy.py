from flask_sqlalchemy import SQLAlchemy

from app import App

class SQLExtension:

    db = SQLAlchemy(App.flask)
    Type = db.Model