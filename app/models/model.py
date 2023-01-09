from app.libs import SQLExtension

class Model(SQLExtension.Type):
    
    __tablename__ = 'Model'
    db = SQLExtension.db
    id = db.Column(db.Integer, primary_key=True)
