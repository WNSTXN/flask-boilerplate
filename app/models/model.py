from flask_sqlalchemy import SQLAlchemy

from app import App


class SQLExtension:

    db = SQLAlchemy(App.flask)
    type = db.Model


class Model(SQLExtension.type):
    
    __tablename__ = 'Model'
    db = SQLExtension.db
    id = db.Column(db.Integer, primary_key=True)
