# app/__init__.py
from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, ma, swagger_init
from .resources.user import user_bp
from .resources.stock import stock_bp
from .utils.error_handlers import register_error_handlers
from .utils.logger import setup_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi ekstensi
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    # Setup logging
    setup_logging(app)

    # Inisialisasi Swagger UI
    swagger_init(app)

    # Register Blueprints
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(stock_bp, url_prefix='/api/stocks')

    # Register error handlers
    register_error_handlers(app)

    return app
