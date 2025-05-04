from flask import Blueprint
from flask_restx import Api
from swagger.namespace.aluno_namespace import alunos_ns
from swagger.namespace.professor_namespace import professores_ns
from swagger.namespace.turma_namespace import turma_ns

# Nome único no blueprint
blueprint = Blueprint('swagger_api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    title="API Escolar",
    version="1.0",
    description="Documentação da API Escolar"
)

api.add_namespace(alunos_ns, path="/alunos")
api.add_namespace(professores_ns, path="/professores")
api.add_namespace(turma_ns, path="/turmas")
api.mask_swagger = False

def configure_swagger(app):
    app.register_blueprint(blueprint)
