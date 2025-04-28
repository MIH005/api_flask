from swagger.namespace.aluno_namespace import aluno_output
from flask_restx import Namespace, Resource, fields
from models.model_turma import adicionar_turma, listar_turmas, buscar_turma_por_id, atualizar_turma, deletar_turma

turma_ns = Namespace("turmas", description="Operações relacionadas às turmas")

model_turma = turma_ns.model("Turma", {
    "descricao": fields.String(required=True, description="Descrição da turma"),
    "professor_id": fields.Integer(required=False, description="ID do professor responsável"),
    "ativo": fields.Boolean(required=False, description="Se a turma está ativa")
})

turma_output_model = turma_ns.model("TurmaOutput", {
    "turma_id": fields.Integer(description="ID da turma"),
    "descricao": fields.String(description="Descrição da turma"),
    "professor_id": fields.Integer(description="ID do professor"),
    "ativo": fields.Boolean(description="Se a turma está ativa"),
    "alunos": fields.List(fields.Nested(aluno_output), description="Lista de alunos da turma")
})

@turma_ns.route("/")
class TurmasResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todas as turmas"""
        return listar_turmas()

    @turma_ns.expect(model_turma)
    def post(self):
        """Cria uma nova turma"""
        data = turma_ns.payload
        response, status_code = adicionar_turma(data)
        return response, status_code

@turma_ns.route("/<int:id_turma>")
class TurmasIdResource(Resource):
    @turma_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Obtém uma turma pelo ID"""
        return buscar_turma_por_id(id_turma)

    @turma_ns.expect(model_turma)
    def put(self, id_turma):
        """Atualiza uma turma pelo ID"""
        data = turma_ns.payload
        atualizar_turma(id_turma, data)
        return data, 200

    def delete(self, id_turma):
        """Exclui uma turma pelo ID"""
        deletar_turma(id_turma)
        return {"message": "Turma excluída com sucesso"}, 200
