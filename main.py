from fastapi import FastAPI

app = FastAPI()

jogos = [
    {
        "id": 1,
        "nome": "Undertale", 
        "descricao": "Jogo indie com elementos de RPG que consiste em exploração, batalhas e escolhas que afetam a historia"
        },
    {
        "id": 2,
        "nome": "Hollow Knight", 
        "descricao": "jogo indie MetroidVania focado na historia e exploração de ambientes contendo alta dificuldade contra inimigos"
        },
    {
        "id": 3, 
        "nome": "Celeste", 
        "descricao": "jogo indie plataforma focado na exploração e na historia contada, jogo baseado em niveis e fases"
        }
]

@app.get("/")
def home():
    return {"mensagem": "API de Jogos Indies"}

@app.get("/jogos")
def listar_jogos():
    return jogos

@app.get("/jogos/{id}")
def buscar_jogo(id: int):
    for jogo in jogos:
        if jogo["id"] == id:
            return jogo

    return {"erro": "Jogo não encontrado"}

@app.get("/pesquisa")
def pesquisar(nome: str):
    resultado = []

    for jogo in jogos:
        if nome.lower() in jogo["nome"].lower():
            resultado.append(jogo)

    return resultado