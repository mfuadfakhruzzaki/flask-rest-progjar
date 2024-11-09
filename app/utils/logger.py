# app/utils/logger.py
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
