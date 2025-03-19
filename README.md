# API REST SISTEMA ESCOLAR

Este projeto implementa uma API REST simples usando o framework Flask e um banco de dados SQLite. A API gerencia informações de professores, alunos e turmas em um sistema escolar.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python, utilizado para criar a API REST.
- **SQLAlchemy**: ORM (Object Relational Mapper) para facilitar o acesso ao banco de dados.
- **SQLite**: Banco de dados simples para armazenar informações.
- **Docker**: Contêiner para rodar a aplicação de forma isolada e garantir a consistência entre ambientes.

## Funcionalidades

- **Cadastro de Professores**: Criar, listar, buscar, atualizar e excluir professores.
- **Cadastro de Alunos**: Criar, listar, buscar, atualizar e excluir alunos.
- **Cadastro de Turmas**: Criar, listar, buscar, atualizar e excluir turmas.
- **Rota de Reset do Banco de Dados**: Restaura o banco de dados, apagando todos os registros e recriando as tabelas.

## Pré-requisitos

Antes de rodar o projeto, você precisa ter o Docker instalado na sua máquina. Caso não tenha o Docker, você pode baixá-lo [aqui](https://www.docker.com/get-started).

### Instalação das dependências

O projeto depende das bibliotecas:

- Flask
- Flask-SQLAlchemy

Essas dependências são gerenciadas através do `Dockerfile` e do `docker-compose.yml`.

## Como Rodar o Projeto Localmente

### 1. Clonando o Repositório

Primeiro, clone o repositório para sua máquina:

```bash
git clone <URL do repositório>
cd <diretório do repositório>
```

### 2. Criar o Contêiner Docker

Com o Docker e Docker Compose instalados, você pode rodar o projeto facilmente com o seguinte comando:

```bash
docker-compose up --build
```

Isso irá:

- Construir a imagem Docker com base no `Dockerfile`.
- Iniciar os containers, incluindo a aplicação Flask e o banco de dados SQLite.

Após alguns instantes, a API estará rodando e acessível em `http://localhost:5000`.

### 3. Acessando a API

A API possui as seguintes rotas:

- **GET /professores**: Retorna todos os professores cadastrados.
- **GET /professores/<id>**: Retorna um professor pelo ID.
- **POST /professores**: Cria um novo professor.
- **PUT /professores/<id>**: Atualiza um professor pelo ID.
- **DELETE /professores/<id>**: Exclui um professor pelo ID.

Rotas semelhantes existem para **alunos** e **turmas**. Veja abaixo as rotas para **alunos** e **turmas**:

- **GET /alunos**: Retorna todos os alunos cadastrados.
- **POST /alunos**: Cria um novo aluno.
- **PUT /alunos/<id>**: Atualiza um aluno pelo ID.
- **DELETE /alunos/<id>**: Exclui um aluno pelo ID.
  
- **GET /turmas**: Retorna todas as turmas cadastradas.
- **POST /turmas**: Cria uma nova turma.
- **PUT /turmas/<id>**: Atualiza uma turma pelo ID.
- **DELETE /turmas/<id>**: Exclui uma turma pelo ID.

Além disso, você pode resetar o banco de dados com a rota:

- **POST /reseta**: Apaga todos os dados e recria o banco de dados.

### 4. Testando as Rotas

Você pode testar as rotas da API usando ferramentas como **Postman** ou **curl**.

**Exemplo de criação de um professor via POST**:

```bash
curl -X POST http://localhost:5000/professores \
     -H "Content-Type: application/json" \
     -d '{"nome": "João Silva", "idade": 35, "materia": "Matemática"}'
```

**Exemplo de atualização de um aluno via PUT**:

```bash
curl -X PUT http://localhost:5000/alunos/1 \
     -H "Content-Type: application/json" \
     -d '{"nome": "Maria Souza", "idade": 18, "nota_primeiro_semestre": 8.5}'
```

### 5. Parar os Contêineres

Para parar os contêineres do Docker, execute:

```bash
docker-compose down
```

### 6. Variáveis de Ambiente

Para configurar variáveis de ambiente, como a URI do banco de dados ou configurações específicas do Flask, você pode editar o arquivo `.env` (caso exista) ou definir variáveis diretamente no Docker Compose.

## Estrutura do Projeto

A estrutura do seu projeto deve ser parecida com esta:

```
.
├── Dockerfile
├── docker-compose.yml
├── app.py (código da aplicação Flask)
├── requirements.txt
└── README.md (este arquivo)
```

### Dockerfile

O `Dockerfile` define como a imagem do Docker será construída. Ele faz o seguinte:

1. Cria uma imagem base usando a imagem oficial do Python.
2. Instala as dependências do projeto.
3. Copia o código da aplicação para dentro do contêiner.
4. Expondo a porta 5000 e rodando o servidor Flask.

### docker-compose.yml

Este arquivo define o serviço Docker para a aplicação. Ele especifica:

- O contêiner para o Flask.
- O mapeamento de portas.
- O volume para persistência de dados no banco de dados SQLite.

