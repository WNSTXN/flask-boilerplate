from flask_sqlalchemy import SQLAlchemy

from app import App

class SQLExtension:
    """
    Summary
    -------
    Static class for SQLAlchemy

    Attributes
    ----------
    db (SQLAlchemy) : SQLAlchemy instance
    Type (type) : SQLAlchemy declarative model class
    """
    db = SQLAlchemy(App.flask)
    Type = db.Model
    