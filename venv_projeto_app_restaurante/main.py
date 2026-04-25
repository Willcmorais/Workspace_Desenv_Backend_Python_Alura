# O fastapi é um módulo e o FastAPI é uma classe desse módulo
from fastapi import FastAPI

# Precisa dessa linha para dar o "start" na fastapi para utilizar
app = FastAPI()


# @app Refere-se à instância do FastAPI criada. .get define o Método HTTP. O GET é usado justamente quando o navegador (ou cliente) quer "buscar" ou "pedir" uma informação. /api/hello é o Caminho (Path). Se o servidor estiver rodando em localhost:8000, a URL completa para acessar essa função será http://localhost:8000/api/hello.
@app.get("/api/hello")
def hello_world():
    # Retornar um dicionário faz com que o navegador receba um JSON: {"message": "Hello World!"}
    return {"message": "Hello World!"}


# para rodar esse código utilizamos no cmd a instrução: uvicorn main:app --reload
