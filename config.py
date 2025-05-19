import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from database.db import db

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///escola.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)


    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return jsonify({"mensagem": "Sistema Escolar Modularizado"})

    @app.route('/reseta', methods=['POST'])
    def resetar_banco():
        try:
            db.drop_all()
            db.create_all()
            return jsonify({"mensagem": "Banco de dados resetado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    return app
