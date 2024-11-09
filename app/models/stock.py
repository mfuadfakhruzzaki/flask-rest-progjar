# app/models/stock.py
from ..extensions import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)
