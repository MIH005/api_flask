from swagger.swagger_config import configure_swagger
from config import Config, create_app
from database.db import db
from routes import professor_blueprint, alunos_blueprint, turma_blueprint
from models import *  # Importa os modelos

app = create_app()  # Agora sim! app é criado aqui

configure_swagger(app)

# Registra blueprints
app.register_blueprint(alunos_blueprint, url_prefix='/api')
app.register_blueprint(turma_blueprint, url_prefix='/api')
app.register_blueprint(professor_blueprint, url_prefix='/api')

# Configura Swagger

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
