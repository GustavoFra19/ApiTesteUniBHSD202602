# Projeto A3: API de Gerenciamento

Esta é a API de backend desenvolvida para o Projeto A3, integrando os conceitos de Sistemas Distribuídos e Usabilidade. A aplicação fornece os endpoints necessários para gerenciar registros e servirá como base de dados para o consumo das interfaces de usuário (front-end).

O projeto foi construído utilizando **FastAPI** e **SQLite**, com uma arquitetura modularizada em múltiplas camadas.

## 🛠 Tecnologias Utilizadas

* **Python 3.8+**
* **FastAPI:** Micro-framework web de alta performance para a construção da API.
* **Uvicorn:** Servidor web ASGI para execução da aplicação.
* **Pydantic:** Validação estrita de dados e tipagem (Type Hints).
* **SQLite:** Banco de dados relacional leve e embutido (persistência local).

## 📁 Arquitetura do Projeto (Múltiplas Camadas)

Para garantir a organização e escalabilidade, o código foi dividido nos seguintes arquivos:

* `database.py`: Gerencia a conexão com o banco de dados SQLite e a criação da tabela.
* `models.py`: Contém os esquemas de dados (Pydantic), separando a entrada de dados (o que o usuário envia) da resposta (o que a API devolve).
* `main.py`: Arquivo principal que concentra as rotas (endpoints HTTP) e a inicialização da API.

## ⚙️ Como Configurar e Executar (Localmente)

1. Clone ou baixe este repositório para a sua máquina local.
2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   # No Windows: venv\Scripts\activate
   # No Linux/Mac: source venv/bin/activate
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install fastapi "uvicorn[standard]"
   ```
4. Inicie o servidor ASGI:
   ```bash
   uvicorn main:app --reload
   ```
5. A API estará rodando no endereço: `http://127.0.0.1:8000`

## ☁️ Como Executar no GitHub Codespaces

1. Na página inicial deste repositório no GitHub, clique no botão verde **Code**.
2. Selecione a aba **Codespaces** e clique em **Create codespace on main**.
3. No terminal integrado do VS Code web, instale as dependências:
   ```bash
   pip install fastapi "uvicorn[standard]"
   ```
4. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```
5. O GitHub exibirá um pop-up. Clique em **Open in Browser** para acessar a aplicação através de uma URL segura gerada dinamicamente.

## 📖 Documentação Automática (Swagger UI)

A API possui documentação nativa e interativa. Com o servidor em execução, acesse o endpoint abaixo no seu navegador:

👉 **`/docs`** (Ex: `http://127.0.0.1:8000/docs`)

Nesta interface, você poderá visualizar o contrato de todos os endpoints e realizar testes práticos utilizando o botão **"Try it out"**.

## 🚀 Endpoints Disponíveis

A API implementa o CRUD completo operando com os status HTTP padronizados (200, 201, 400, 404, 500):

* `POST /registros`: Cria um novo registro no banco de dados.
* `GET /registros`: Retorna a lista de todos os registros.
* `GET /registros/{id}`: Busca os detalhes de um registro específico pelo ID.
* `PUT /registros/{id}`: Atualiza os dados de um registro existente.
* `DELETE /registros/{id}`: Exclui um registro do sistema.
