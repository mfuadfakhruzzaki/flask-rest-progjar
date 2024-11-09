# app/resources/stock.py
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from ..services.stock_service import StockService
from ..schemas.stock import StockSchema
from flask_jwt_extended import jwt_required

stock_bp = Blueprint('stock_bp', __name__)
api = Api(stock_bp)
stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)

class AddStockResource(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        errors = stock_schema.validate(data)
        if errors:
            return {'errors': errors}, 400

        item_name = data.get('item_name')
        quantity = data.get('quantity', 0)
        stock = StockService.add_stock(item_name, quantity)
        return stock_schema.dump(stock), 200

class RemoveStockResource(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        item_name = data.get('item_name')
        quantity = data.get('quantity', 0)

        if not item_name or quantity < 0:
            return {'message': 'Valid item name and quantity are required'}, 400

        stock, error = StockService.remove_stock(item_name, quantity)
        if error:
            return {'message': error}, 400

        return stock_schema.dump(stock), 200

class CheckStockResource(Resource):
    @jwt_required()
    def get(self):
        stocks = StockService.get_all_stocks()
        return stocks_schema.dump(stocks), 200

class DeleteStockResource(Resource):
    @jwt_required()
    def delete(self):
        data = request.get_json()
        item_name = data.get('item_name')

        if not item_name:
            return {'message': 'Item name is required'}, 400

        stock, error = StockService.delete_stock(item_name)
        if error:
            return {'message': error}, 404

        return {'message': 'Stock deleted successfully'}, 200

# Register resources
api.add_resource(AddStockResource, '/add')
api.add_resource(RemoveStockResource, '/remove')
api.add_resource(CheckStockResource, '/check')
api.add_resource(DeleteStockResource, '/delete')
