from flask import Blueprint, request, jsonify
from models.model_turma import adicionar_turma, listar_turmas, buscar_turma_por_id, atualizar_turma, deletar_turma

turma_blueprint = Blueprint('turma', __name__)

# Adicionar turma
@turma_blueprint.route('/turmas', methods=['POST'])
def rota_adicionar_turma():
    return adicionar_turma()

# Listar turmas
@turma_blueprint.route('/turmas', methods=['GET'])
def rota_listar_turmas():
    return listar_turmas()

# Buscar turma por ID
@turma_blueprint.route('/turmas/<int:id>', methods=['GET'])
def rota_buscar_turma_por_id(id):
    return buscar_turma_por_id(id)

# Atualizar turma
@turma_blueprint.route('/turmas/<int:id>', methods=['PUT'])
def rota_atualizar_turma(id):
    return atualizar_turma(id)

# Deletar turma
@turma_blueprint.route('/turmas/<int:id>', methods=['DELETE'])
def rota_deletar_turma(id):
    return deletar_turma(id)
