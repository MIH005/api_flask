from flask import request, jsonify
from database.db import db

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=True)
    turma = db.relationship('Turma', backref='professores', foreign_keys=[turma_id])

def criar_professor():
    dados = request.json

    if "nome" not in dados or "idade" not in dados or "materia" not in dados:
        return jsonify({"erro": "Campos obrigatórios: nome, idade, materia"}), 400

    novo_professor = Professor(
        nome=dados['nome'],
        idade=dados['idade'],
        materia=dados['materia'],
        observacoes=dados.get('observacoes', ''),
        turma_id=dados.get('turma_id')
    )

    db.session.add(novo_professor)
    db.session.commit()

    return jsonify({
        "mensagem": "Professor cadastrado com sucesso!",
        "id": novo_professor.id 
    }), 201

def listar_professores():
    professores = Professor.query.all()
    resultado = [
        {
            "id": p.id, 
            "nome": p.nome, 
            "idade": p.idade, 
            "materia": p.materia, 
            "turma": {
                "id": p.turma.id if p.turma else None,
                "descricao": p.turma.descricao if p.turma else None
            },
            "observacoes": p.observacoes
        }
        for p in professores
    ]
    return jsonify(resultado)

def buscar_professor(id):
    professor = db.session.get(Professor, id) 

    if not professor:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    resultado = {
        "id": professor.id, 
        "nome": professor.nome, 
        "idade": professor.idade, 
        "materia": professor.materia, 
        "turma": {
            "id": professor.turma.id if professor.turma else None,
            "descricao": professor.turma.descricao if professor.turma else None
        },
        "observacoes": professor.observacoes
    }

    return jsonify(resultado)

def atualizar_professor(id):
    professor = Professor.query.get_or_404(id, description="Professor não encontrado.")

    dados = request.json
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    professor.nome = dados.get('nome', professor.nome)
    professor.idade = dados.get('idade', professor.idade)
    professor.materia = dados.get('materia', professor.materia)
    professor.turma_id = dados.get('turma_id', professor.turma_id)
    professor.observacoes = dados.get('observacoes', professor.observacoes)

    db.session.commit()
    return jsonify({"mensagem": "Professor atualizado com sucesso!"})

def deletar_professor(id):
    professor = db.session.get(Professor, id)

    if not professor:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    db.session.delete(professor)
    db.session.commit()
    return jsonify({"mensagem": "Professor deletado com sucesso!"})