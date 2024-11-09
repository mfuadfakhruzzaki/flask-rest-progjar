# app/schemas/stock.py
from ..extensions import ma
from ..models.stock import Stock
from marshmallow import fields, validate

class StockSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stock
        load_instance = True

    item_name = fields.String(required=True, validate=validate.Length(min=1))
    quantity = fields.Integer(required=True, validate=validate.Range(min=0))
