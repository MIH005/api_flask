from flask import Blueprint, request, jsonify
from models.model_aluno import criar_aluno, listar_alunos, buscar_aluno, atualizar_aluno, deletar_aluno

alunos_blueprint = Blueprint('alunos', __name__)

# Rota para adicionar aluno
@alunos_blueprint.route('/alunos', methods=['POST'])
def rota_adicionar_aluno():
    return criar_aluno()

# Rota para listar todos os alunos
@alunos_blueprint.route('/alunos', methods=['GET'])
def rota_listar_alunos():
    return listar_alunos()

# Rota para buscar aluno por ID
@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def rota_buscar_aluno(id_aluno):
    return buscar_aluno(id_aluno)

# Rota para atualizar aluno
@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def rota_atualizar_aluno(id_aluno):
    return atualizar_aluno(id_aluno)

# Rota para deletar aluno
@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def rota_deletar_aluno(id_aluno):
    return deletar_aluno(id_aluno)
