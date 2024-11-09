# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()

def swagger_init(app):
    SWAGGER_URL = app.config['SWAGGER_URL']  # e.g., /api/docs
    API_URL = app.config['API_URL']  # e.g., /static/swagger.json
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Flask REST API"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
