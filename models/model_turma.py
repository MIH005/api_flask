from flask import request, jsonify
from database.db import db
from models.model_professor import Professor


class Turma(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id', ondelete="SET NULL"), nullable=True)
    ativo = db.Column(db.Boolean, default=True)
    alunos = db.relationship('Aluno', backref='turma', lazy=True)


def adicionar_turma():
    dados = request.json

    descricao = dados.get('descricao')
    if not descricao or len(descricao.strip()) < 3:
        return jsonify({'erro': 'Descrição inválida. Informe pelo menos 3 caracteres.'}), 400

    professor_id = dados.get('professor_id')
    if professor_id:
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({"erro": "Professor não encontrado"}), 404

    nova_turma = Turma(
        descricao=descricao.strip(),
        professor_id=professor_id,
        ativo=dados.get('ativo', True)
    )

    db.session.add(nova_turma)
    db.session.commit()

    return jsonify({'mensagem': 'Turma adicionada com sucesso!', 'id': nova_turma.id}), 201


def listar_turmas():
    # Descomente abaixo se quiser listar apenas turmas ativas
    # turmas = Turma.query.filter_by(ativo=True).all()
    turmas = Turma.query.all()

    resultado = []
    for turma in turmas:
        resultado.append({
            'turma_id': turma.id,
            'descricao': turma.descricao,
            'professor_id': turma.professor_id,
            'ativo': turma.ativo,
            'alunos': [{'id': aluno.id, 'nome': aluno.nome} for aluno in turma.alunos]
        })
    return jsonify(resultado)


def buscar_turma_por_id(id):
    turma = db.session.get(Turma, id)

    if turma:
        return jsonify({
            'id': turma.id,
            'descricao': turma.descricao,
            'professor_id': turma.professor_id,
            'ativo': turma.ativo,
            'alunos': [{'id': aluno.id, 'nome': aluno.nome} for aluno in turma.alunos]
        })

    return jsonify({'mensagem': 'Turma não encontrada'}), 404


def atualizar_turma(id):
    turma = db.session.get(Turma, id)

    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    dados = request.json

    if 'descricao' in dados:
        nova_descricao = dados['descricao'].strip()
        if len(nova_descricao) < 3:
            return jsonify({'erro': 'Descrição muito curta. Mínimo 3 caracteres.'}), 400
        turma.descricao = nova_descricao

    if 'professor_id' in dados:
        professor_id = dados['professor_id']
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({"erro": "Professor não encontrado"}), 404
        turma.professor_id = professor_id

    if 'ativo' in dados:
        turma.ativo = dados['ativo']

    db.session.commit()
    return jsonify({"mensagem": "Turma atualizada com sucesso!"})


def deletar_turma(id):
    turma = db.session.get(Turma, id)

    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    db.session.delete(turma)
    db.session.commit()
    return jsonify({"mensagem": "Turma deletada com sucesso!"})
