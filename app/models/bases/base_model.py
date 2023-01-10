from dataclasses import dataclass

from app.libs import SQLExtension


@dataclass
class BaseModel(SQLExtension.Type):
    __abstract__ = True
    db = SQLExtension.db

    id: int = db.Column(db.Integer, primary_key=True)