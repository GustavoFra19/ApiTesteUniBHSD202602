# Documentação - Refatoração para Multicamadas 

Repositório (fork): https://github.com/GustavoFra19/ApiTesteUniBHSD202602
Branch: multicamadas
Link: https://github.com/GustavoFra19/ApiTesteUniBHSD202602/tree/multicamadas

## Ambiente
GitHub Codespaces, Python 3.14, uv, FastAPI, Uvicorn, SQLite.

## O que foi feito
1. Fork do repositório fvaladares/ApitUniBHSD202602 e abertura no Codespaces.
2. Instalação do uv (pip install uv) e do uvicorn (uv add uvicorn), que não constava nas dependências do pyproject.toml.
3. Execução da versão monolítica (uv run uvicorn App:app --reload) e teste do POST /registros no Swagger (/docs): retorno 201.
4. Criação da branch "multicamadas" (git checkout -b multicamadas).
5. Renomeação de App.py para main.py (git mv), conforme o README do projeto.
6. Criação do database.py: funções conectar_banco() e criar_tabelas() (camada de dados).
7. Criação do models.py: classes RegistroBase e RegistroResponse (camada de modelos Pydantic).
8. Refatoração do main.py: mantém apenas a inicialização do FastAPI, o evento de startup e as rotas, importando database e models.
9. Execução da versão multicamadas (uv run uvicorn main:app --reload).
10. Testes dos 5 endpoints no Swagger, com os resultados esperados:
    - POST /registros: 201
    - GET /registros: 200
    - GET /registros/{id}: 200 (existente) e 404 (inexistente)
    - PUT /registros/{id}: 200
    - DELETE /registros/{id}: 200 e 404 (inexistente)
11. Atualização do .gitignore (banco_a3.db, .venv/, __pycache__/), commit e push da branch.

## Estrutura final
├── main.py       # rotas e inicialização da API
├── database.py   # conexão com SQLite e criação de tabelas
├── models.py     # modelos Pydantic
└── pyproject.toml

## Observações
- O comportamento da API é idêntico ao da versão monolítica; mudou apenas a organização do código.
- Durante a execução, o erro "ModuleNotFoundError: No module named 'models'" ocorreu por o arquivo models.py ainda não ter sido criado; foi resolvido ao criá-lo na raiz do projeto.
