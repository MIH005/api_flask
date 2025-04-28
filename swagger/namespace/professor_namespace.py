from flask_restx import Namespace, Resource, fields
from models.model_professor import criar_professor, listar_professores, buscar_professor, atualizar_professor, deletar_professor

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

model_professor = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "materia": fields.String(required=True, description="Materia do professor"),
    "observacoes": fields.String(description="Observações sobre o professor")

})  

professor_output_model = professores_ns.model("ProfessorOutput",{
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(required=True, description="Nome do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "materia": fields.String(required=True, description="Materia do professor"),
        "turma": fields.Nested(professores_ns.model('Turma', {
        "id": fields.Integer(description="ID da turma"),
        "descricao": fields.String(description="Descrição da turma"),
    })),
    "observacoes": fields.String(description="Observações sobre o professor")
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return listar_professores()

    @professores_ns.expect(model_professor)
    def post(self):
        """Cria um novo professor"""
        data = professores_ns.payload
        response, status_code = criar_professor(data)
        return response, status_code

@professores_ns.route("/<int:id_professor>")
class ProfessoresIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return buscar_professor(id_professor)

    @professores_ns.expect(model_professor)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professores_ns.payload
        atualizar_professor(id_professor, data)
        return data, 200

    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        deletar_professor(id_professor)
        return {"message": "Professor excluído com sucesso"}, 200
