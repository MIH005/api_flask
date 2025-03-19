import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestProfessores(unittest.TestCase):
    def setUp(self):
        """Reseta o banco antes de cada teste, se a rota existir"""
        try:
            requests.post(f"{BASE_URL}/reseta")
        except requests.exceptions.RequestException:
            print(" Aviso: A rota /reseta não existe ou não está acessível.")

    def test_001_criar_professor(self):
        
        professor = {
            "nome": "Dr. João",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Especialista em álgebra"
        }
        response = requests.post(f"{BASE_URL}/professores", json=professor)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())  

    def test_002_listar_professores(self):
 
        professor = {
            "nome": "Dr. Marcos",
            "idade": 40,
            "materia": "Fisica",
            "observacoes": "professor senior"
        }
        requests.post(f"{BASE_URL}/professores", json=professor)

        response = requests.get(f"{BASE_URL}/professores")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)  



    def test_003_get_professor_por_id(self):

        professor = {
            "nome": "Dr. João",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Especialista em álgebra"
        }

        response_post = requests.post(f"{BASE_URL}/professores", json=professor)
        self.assertEqual(response_post.status_code, 201)
        
        professor_id = response_post.json().get("id")
        self.assertIsNotNone(professor_id, "Erro: ID não retornado")

        response_get = requests.get(f"{BASE_URL}/professores/{professor_id}")
        self.assertEqual(response_get.status_code, 200)

        data = response_get.json()
        self.assertEqual(data["id"], professor_id)
        self.assertEqual(data["nome"], professor["nome"])
        self.assertEqual(data["idade"], professor["idade"])
        self.assertEqual(data["materia"], professor["materia"])
        self.assertEqual(data["observacoes"], professor["observacoes"])

    def test_004_deletar_professor(self):

        professor = {
            "nome": "Dr. José",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Professor de álgebra"
        }
        
        response_post = requests.post(f"{BASE_URL}/professores", json=professor)
        self.assertEqual(response_post.status_code, 201)  

        professor_id = response_post.json()["id"]
        
        response_delete = requests.delete(f"{BASE_URL}/professores/{professor_id}")
        self.assertEqual(response_delete.status_code, 200)  


    def test_005_atualizar_professor(self):

        professor_criado = {
            "nome": "Prof. João",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Professor experiente"
        }

        response_criar = requests.post(f"{BASE_URL}/professores", json=professor_criado)
        self.assertEqual(response_criar.status_code, 201)

        professor_id = response_criar.json()['id']

        professor_atualizado = {
            "nome": "Prof. João Atualizado",
            "idade": 41,
            "materia": "Física",
            "observacoes": "Professor com novas observações"
        }

        response_atualizar = requests.post(f"{BASE_URL}/professores/{professor_id}", json=professor_atualizado)

        self.assertEqual(response_atualizar.status_code, 200)
        self.assertEqual(response_atualizar.json(), {"mensagem": "Professor atualizado com sucesso!"})

        response_verificar = requests.get(f"{BASE_URL}/professores/{professor_id}")
        professor_verificado = response_verificar.json()

        self.assertEqual(professor_verificado['nome'], "Prof. João Atualizado")
        self.assertEqual(professor_verificado['idade'], 41)
        self.assertEqual(professor_verificado['materia'], "Física")
        self.assertEqual(professor_verificado['observacoes'], "Professor com novas observações")


class TestTurmas(unittest.TestCase):
    def setUp(self):
        """Reseta o banco antes de cada teste, se a rota existir"""
        try:
            requests.post(f"{BASE_URL}/reseta")
        except requests.exceptions.RequestException:
            print(" Aviso: A rota /reseta não existe ou não está acessível.")

    def test_006_criar_turma(self):
        turma = {
            "descricao": "9° Ano",
            "professor_id": 1,
            "ativo": True,
            "alunos": [{"nome": "João"}, {"nome": "Maria"}, {"nome": "Ana"}]
        }
        response = requests.post(f"{BASE_URL}/turmas", json=turma)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_007_listar_turmas(self):

        professor = {
            "descricao": "3° Ano",
            "professor_id": 2,
            "ativo": True,
            "alunos": [{"nome": "Camilla"}, {"nome": "João"}, {"nome": "Maria"}]    
        }
        requests.post(f"{BASE_URL}/turmas", json=professor)

        response = requests.get(f"{BASE_URL}/turmas")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_008_buscar_turma_por_id(self):
        
        professor_criado = {
            "nome": "Prof. João",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Professor experiente"
        }
        
        response_criar_professor = requests.post(f"{BASE_URL}/professores", json=professor_criado)
        self.assertEqual(response_criar_professor.status_code, 201)

        turma_criada = {
            "descricao": "1° Ano",
            "professor_id": 1,  
            "ativo": True
        }

        response_criar = requests.post(f"{BASE_URL}/turmas", json=turma_criada)
        self.assertEqual(response_criar.status_code, 201)

        turma_id = response_criar.json()["id"]
        
        response_buscar = requests.get(f"{BASE_URL}/turmas/{turma_id}")
        
        self.assertEqual(response_buscar.status_code, 200)
        
        turma = response_buscar.json()
        self.assertEqual(turma['id'], turma_id)
        self.assertEqual(turma['descricao'], turma_criada['descricao'])
        self.assertEqual(turma['professor_id'], turma_criada['professor_id'])
        self.assertEqual(turma['ativo'], turma_criada['ativo'])
        self.assertEqual(turma['alunos'], [])  

        
    def test_009_deletar_turma(self):
            turma = {
            "descricao": "8° Ano",
            "professor_id": 4,
            "ativo": True,
            "alunos": [  
            {"nome": "kaka"},
            {"nome": "Ana"},
            {"nome": "Bruna"}
        ]
        }
            response_post = requests.post(f"{BASE_URL}/turmas", json=turma)
            self.assertEqual(response_post.status_code, 201)  
        
            turma_id = response_post.json()["id"]
        
            response_delete = requests.delete(f"{BASE_URL}/turmas/{turma_id}")
            self.assertEqual(response_delete.status_code, 200)  


    def test_010_atualizar_turma(self):

        professor_criado = {
            "nome": "Prof. João",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Professor experiente"
        }
        
        response_professor = requests.post(f"{BASE_URL}/professores", json=professor_criado)
        self.assertEqual(response_professor.status_code, 201)

        professor_id = response_professor.json()['id']

        turma_criada = {
            "descricao": "Turma de Matemática",
            "professor_id": professor_id, 
            "ativo": True
        }

        response_criar = requests.post(f"{BASE_URL}/turmas", json=turma_criada)
        self.assertEqual(response_criar.status_code, 201)

        turma_id = response_criar.json()['id']
        self.assertIsNotNone(turma_id, "ID da turma não foi retornado corretamente")

        turma_atualizada = {
            "descricao": "Turma de Física",
            "professor_id": professor_id,  
            "ativo": False
        }

        response_atualizar = requests.put(f"{BASE_URL}/turmas/{turma_id}", json=turma_atualizada)
        print(f"Status Code da Atualização: {response_atualizar.status_code}")

        self.assertEqual(response_atualizar.status_code, 200)
        self.assertEqual(response_atualizar.json(), {"mensagem": "Turma atualizada com sucesso!"})

        response_verificar = requests.get(f"{BASE_URL}/turmas/{turma_id}")
        turma_verificada = response_verificar.json()

        self.assertEqual(turma_verificada['descricao'], "Turma de Física")
        self.assertEqual(turma_verificada['professor_id'], professor_id)  
        self.assertEqual(turma_verificada['ativo'], False)


class TestAlunos(unittest.TestCase):
    def setUp(self):
        """Reseta o banco antes de cada teste, se a rota existir"""
        try:
            requests.post(f"{BASE_URL}/reseta")
        except requests.exceptions.RequestException:
            print(" Aviso: A rota /reseta não existe ou não está acessível.")

    def test_001_criar_aluno_sem_turma(self):
        """Testa a criação de um aluno sem turma"""
        aluno = {
            "nome": "João Silva",
            "idade": 17,
            "data_nascimento": "01-01-2006",
            "nota_primeiro_semestre": 7.5,
            "nota_segundo_semestre": 8.0,
            "media_final": 7.75
        }
        response = requests.post(f"{BASE_URL}/alunos", json=aluno)
        self.assertEqual(response.status_code, 201)
        self.assertIn("mensagem", response.json())


    def test_012_listar_alunos(self):

        aluno = {
            "nome": "Maria Souza",
            "idade": 18,
            "data_nascimento": "15-03-2005",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 8.5,
            "media_final": 8.75
        }
        requests.post(f"{BASE_URL}/alunos", json=aluno)

        response = requests.get(f"{BASE_URL}/alunos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_013_get_aluno_por_id(self):
        """Cria um aluno e busca pelo ID"""
        aluno = {
            "nome": "Carlos Oliveira",
            "idade": 19,
            "data_nascimento": "22-11-2004",
            "nota_primeiro_semestre": 6.5,
            "nota_segundo_semestre": 7.0,
            "media_final": 6.75
        }

        response_post = requests.post(f"{BASE_URL}/alunos", json=aluno)
        self.assertEqual(response_post.status_code, 201)

        aluno_id = response_post.json().get("id")
        self.assertIsNotNone(aluno_id, "Erro: ID não retornado")

        response_get = requests.get(f"{BASE_URL}/alunos/{aluno_id}")
        self.assertEqual(response_get.status_code, 200)

        data = response_get.json()
        self.assertEqual(data["id"], aluno_id)
        self.assertEqual(data["nome"], aluno["nome"])
        self.assertEqual(data["idade"], aluno["idade"])
        self.assertEqual(data["data_nascimento"], aluno["data_nascimento"])

    def test_014_deletar_aluno(self):
        aluno = {
            "nome": "Ana Costa",
            "idade": 20,
            "data_nascimento": "10-08-2003",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 9.0,
            "media_final": 8.75
        }
        
        response_post = requests.post(f"{BASE_URL}/alunos", json=aluno)
        self.assertEqual(response_post.status_code, 201)  
        
        aluno_id = response_post.json()["id"]
        
        response_delete = requests.delete(f"{BASE_URL}/alunos/{aluno_id}")
        self.assertEqual(response_delete.status_code, 200)  

    def test_015_atualizar_aluno(self):
        aluno = {
            "nome": "Lucas Pereira",
            "idade": 17,
            "data_nascimento": "25-05-2006",
            "nota_primeiro_semestre": 6.0,
            "nota_segundo_semestre": 7.0,
            "media_final": 6.5
        }

        response_criar = requests.post(f"{BASE_URL}/alunos", json=aluno)
        self.assertEqual(response_criar.status_code, 201)

        aluno_id = response_criar.json()['id']

        aluno_atualizado = {
            "nome": "Lucas Pereira Atualizado",
            "idade": 18,
            "data_nascimento": "25-05-2005",
            "nota_primeiro_semestre": 7.5,
            "nota_segundo_semestre": 8.0,
            "media_final": 7.75
        }

        response_atualizar = requests.put(f"{BASE_URL}/alunos/{aluno_id}", json=aluno_atualizado)

        self.assertEqual(response_atualizar.status_code, 200)
        self.assertEqual(response_atualizar.json(), {"mensagem": "Aluno atualizado com sucesso!"})

        response_verificar = requests.get(f"{BASE_URL}/alunos/{aluno_id}")
        aluno_verificado = response_verificar.json()

        self.assertEqual(aluno_verificado['nome'], "Lucas Pereira Atualizado")
        self.assertEqual(aluno_verificado['idade'], 18)
        self.assertEqual(aluno_verificado['data_nascimento'], "25-05-2005")
        self.assertEqual(aluno_verificado['nota_primeiro_semestre'], 7.5)
        self.assertEqual(aluno_verificado['nota_segundo_semestre'], 8.0)

if __name__ == "__main__":
    unittest.main()
