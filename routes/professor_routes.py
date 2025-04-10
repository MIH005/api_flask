from flask import Blueprint, request, jsonify
from models.model_professor import criar_professor, listar_professores, buscar_professor, atualizar_professor, deletar_professor

professor_blueprint = Blueprint('professor', __name__)

#add prof
@professor_blueprint.route('/professores', methods=['POST'])
def rota_adicionar_professor():
    dados = request.json

    return criar_professor()

#listar
@professor_blueprint.route('/professores', methods=['GET'])
def rota_listar_professores():
    return listar_professores()

#buscar 
@professor_blueprint.route('/professores/<int:id>', methods=['GET'])
def rota_buscar_professores(id):
    return buscar_professor(id)

#att 
@professor_blueprint.route('/professores/<int:id>', methods=['PUT'])
def rota_atualizar_professor(id):
    dados = request.json

    return atualizar_professor(id)

#delete
@professor_blueprint.route('/professores/<int:id>', methods=['DELETE'])
def rota_deletar_professor(id):
    return deletar_professor(id)



