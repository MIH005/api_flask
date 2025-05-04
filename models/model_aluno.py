from database.db import db
from models.model_turma import Turma 
from datetime import datetime
from flask import request, jsonify

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id', ondelete="SET NULL"), nullable=True)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)



def criar_aluno():
    dados = request.json  # necessário!

    turma_id = dados.get('turma_id')  
    turma = None

    if turma_id:
        turma = Turma.query.get(turma_id)
        if not turma:
            return jsonify({"erro": "Turma não encontrada"}), 404

    data_nascimento = datetime.strptime(dados['data_nascimento'], '%d-%m-%Y').date()

    novo_aluno = Aluno(
        nome=dados['nome'],
        idade=dados['idade'],
        turma_id=turma.id if turma else None,
        data_nascimento=data_nascimento,
        nota_primeiro_semestre=dados.get('nota_primeiro_semestre'),
        nota_segundo_semestre=dados.get('nota_segundo_semestre'),
        media_final=dados.get('media_final')
    )

    db.session.add(novo_aluno)
    db.session.commit()
    
    return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "id": novo_aluno.id}), 201


def listar_alunos():
    alunos = Aluno.query.all()
    resultado = [
        {
            "id": a.id,
            "nome": a.nome,
            "idade": a.idade,
            "turma": {"id": a.turma.id, "descricao": a.turma.descricao} if a.turma else None,
            'data_nascimento': a.data_nascimento.strftime('%d-%m-%Y'),
            "nota_primeiro_semestre": a.nota_primeiro_semestre,
            "nota_segundo_semestre": a.nota_segundo_semestre,
            "media_final": a.media_final
        }
        for a in alunos
    ]
    return jsonify(resultado)


def buscar_aluno(id):
    aluno = db.session.get(Aluno, id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    resultado = {
        "id": aluno.id,
        "nome": aluno.nome,
        "idade": aluno.idade,
        "turma": {"id": aluno.turma.id, "descricao": aluno.turma.descricao} if aluno.turma else None,
        'data_nascimento': aluno.data_nascimento.strftime('%d-%m-%Y'),
        "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
        "nota_segundo_semestre": aluno.nota_segundo_semestre,
        "media_final": aluno.media_final
    }

    return jsonify(resultado)


def atualizar_aluno(id):
    aluno = db.session.get(Aluno, id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    dados = request.json

    if 'turma_id' in dados:
        turma = Turma.query.get(dados['turma_id'])
        if not turma:
            return jsonify({"erro": "Turma não encontrada"}), 404
        aluno.turma_id = turma.id

    aluno.nome = dados.get('nome', aluno.nome)
    aluno.idade = dados.get('idade', aluno.idade)

    if 'data_nascimento' in dados:
        aluno.data_nascimento = datetime.strptime(dados['data_nascimento'], '%d-%m-%Y').date()

    aluno.nota_primeiro_semestre = dados.get('nota_primeiro_semestre', aluno.nota_primeiro_semestre)
    aluno.nota_segundo_semestre = dados.get('nota_segundo_semestre', aluno.nota_segundo_semestre)
    aluno.media_final = dados.get('media_final', aluno.media_final)

    db.session.commit()
    return jsonify({"mensagem": "Aluno atualizado com sucesso!"})


def deletar_aluno(id):
    aluno = db.session.get(Aluno, id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"mensagem": "Aluno deletado com sucesso!"})
