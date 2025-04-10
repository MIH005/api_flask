from flask import Flask, jsonify
from config import Config
from database.db import db
from routes import professor_blueprint, alunos_blueprint, turma_blueprint
from models import *  # Importa os modelos

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(professor_blueprint)
    app.register_blueprint(alunos_blueprint)
    app.register_blueprint(turma_blueprint)

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

    return app  # Isso deve vir por último

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
