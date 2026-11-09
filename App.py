import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API de Gerenciamento - Projeto A3",
    description="Template inicial integrando FastAPI, SQLite e validações Pydantic.",
    version="1.0.0"
)


# ==========================================
# 1. CAMADA DE BANCO DE DADOS (SQLite)
# ==========================================
def get_db_connection():
    # Cria o arquivo banco_a3.db na mesma pasta do projeto
    conn = sqlite3.connect("banco_a3.db")
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn


# Cria a tabela automaticamente ao iniciar a API
@app.on_event("startup")
def startup_event():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            ativo BOOLEAN DEFAULT TRUE
        )
    ''')
    conn.commit()
    conn.close()


# ==========================================
# 2. CAMADA DE MODELOS (Pydantic)
# ==========================================
class RegistroBase(BaseModel):
    titulo: str
    descricao: str | None = None
    ativo: bool = True


class RegistroResponse(RegistroBase):
    id: int


# ==========================================
# 3. CAMADA DE ROTAS (Endpoints HTTP)
# ==========================================

@app.post("/registros", response_model=RegistroResponse, status_code=201)
def criar_registro(registro: RegistroBase):
    # Requisito 5: Código 400 (Bad Request) para regra de negócio inválida
    if not registro.titulo.strip():
        raise HTTPException(status_code=400, detail="O título não pode estar em branco.")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registros (titulo, descricao, ativo) VALUES (?, ?, ?)",
            (registro.titulo, registro.descricao, registro.ativo)
        )
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()

        return {**registro.model_dump(), "id": novo_id}
    except Exception as e:
        # Requisito 5: Código 500 (Internal Server Error)
        raise HTTPException(status_code=500, detail=f"Erro interno no banco de dados: {str(e)}")


@app.get("/registros", response_model=list[RegistroResponse], status_code=200)
def listar_registros():
    conn = get_db_connection()
    registros = conn.execute("SELECT * FROM registros").fetchall()
    conn.close()
    return [dict(reg) for reg in registros]


@app.get("/registros/{registro_id}", response_model=RegistroResponse, status_code=200)
def buscar_registro(registro_id: int):
    conn = get_db_connection()
    registro = conn.execute("SELECT * FROM registros WHERE id = ?", (registro_id,)).fetchone()
    conn.close()

    if registro is None:
        # Requisito 5: Código 404 (Not Found)
        raise HTTPException(status_code=404, detail="Registro não encontrado.")

    return dict(registro)


@app.put("/registros/{registro_id}", response_model=RegistroResponse, status_code=200)
def atualizar_registro(registro_id: int, registro: RegistroBase):
    conn = get_db_connection()
    existente = conn.execute("SELECT * FROM registros WHERE id = ?", (registro_id,)).fetchone()

    if existente is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Registro não encontrado para atualização.")

    try:
        conn.execute(
            "UPDATE registros SET titulo = ?, descricao = ?, ativo = ? WHERE id = ?",
            (registro.titulo, registro.descricao, registro.ativo, registro_id)
        )
        conn.commit()
        conn.close()
        return {**registro.model_dump(), "id": registro_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


@app.delete("/registros/{registro_id}", status_code=200)
def deletar_registro(registro_id: int):
    conn = get_db_connection()
    existente = conn.execute("SELECT * FROM registros WHERE id = ?", (registro_id,)).fetchone()

    if existente is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Registro não encontrado para exclusão.")

    conn.execute("DELETE FROM registros WHERE id = ?", (registro_id,))
    conn.commit()
    conn.close()

    return {"mensagem": "Registro removido com sucesso."}