from flask_sqlalchemy import SQLAlchemy

from app import App


class SQLExtension:

    db = SQLAlchemy(App.flask)
    type = db.Model


class Model(SQLExtension.type):
    
    __tablename__ = 'Model'
    id = SQLExtension.db.Column(SQLExtension.db.Integer, primary_key=True)