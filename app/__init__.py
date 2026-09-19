from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from app.database import init_db
from app.routes import api, pages


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins=app.config['CORS_ORIGINS'])

    init_db(app)

    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/health')
    def health():
        return jsonify({"durum": "aktif"}), 200

    return app

