from db import db

class TagModel(db.Model):
    __tablename__ = "tags"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False) # el nombre se puso unique=True pero también puede ponerse falso y revisar manualmente que no hayan dos iguales.
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    
    store = db.relationship("StoreModel", back_populates="tags")
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")