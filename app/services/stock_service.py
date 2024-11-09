# app/services/stock_service.py
from ..models.stock import Stock
from ..extensions import db

class StockService:
    @staticmethod
    def add_stock(item_name, quantity):
        stock = Stock.query.filter_by(item_name=item_name).first()
        if stock:
            stock.quantity += quantity
        else:
            stock = Stock(item_name=item_name, quantity=quantity)
            db.session.add(stock)
        db.session.commit()
        return stock

    @staticmethod
    def remove_stock(item_name, quantity):
        stock = Stock.query.filter_by(item_name=item_name).first()
        if not stock:
            return None, "Item not found"

        if stock.quantity < quantity:
            return None, "Insufficient stock"

        stock.quantity -= quantity
        db.session.commit()
        return stock, None

    @staticmethod
    def get_all_stocks():
        return Stock.query.all()

    @staticmethod
    def delete_stock(item_name):
        stock = Stock.query.filter_by(item_name=item_name).first()
        if not stock:
            return None, "Item not found"
        db.session.delete(stock)
        db.session.commit()
        return stock, None
