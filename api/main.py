from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Permite acesso do seu site
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir imagens da pasta assets
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

jogos = [
    {
        "id": 1,
        "nome": "Undertale",
        "ano": 2015,
        "genero": "RPG",
        "desenvolvedora": "Toby Fox",
        "descricao": "RPG onde escolhas afetam a história e os combates.",
        "imagem": "/assets/undertale.png"
    },
    {
        "id": 2,
        "nome": "Hollow Knight",
        "ano": 2017,
        "genero": "Metroidvania",
        "desenvolvedora": "Team Cherry",
        "descricao": "Exploração, combate desafiador e um vasto reino subterrâneo.",
        "imagem": "/assets/hollow-knight.png"
    },
    {
        "id": 3,
        "nome": "Celeste",
        "ano": 2018,
        "genero": "Plataforma",
        "desenvolvedora": "Maddy Makes Games",
        "descricao": "Plataforma precisa com narrativa emocionante.",
        "imagem": "/assets/celeste.png"
    },
    {
        "id": 4,
        "nome": "Stardew Valley",
        "ano": 2016,
        "genero": "Simulação",
        "desenvolvedora": "ConcernedApe",
        "descricao": "Gerencie uma fazenda e construa relacionamentos.",
        "imagem": "/assets/stardew-valley.png"
    },
    {
        "id": 5,
        "nome": "Terraria",
        "ano": 2011,
        "genero": "Sandbox",
        "desenvolvedora": "Re-Logic",
        "descricao": "Exploração, construção e combate em mundo 2D.",
        "imagem": "/assets/terraria.png"
    },
    {
        "id": 6,
        "nome": "Cuphead",
        "ano": 2017,
        "genero": "Run and Gun",
        "desenvolvedora": "Studio MDHR",
        "descricao": "Combates contra chefes com visual inspirado em desenhos antigos.",
        "imagem": "/assets/cuphead.png"
    },
    {
        "id": 7,
        "nome": "Dead Cells",
        "ano": 2018,
        "genero": "Roguelike",
        "desenvolvedora": "Motion Twin",
        "descricao": "Ação rápida com mapas gerados proceduralmente.",
        "imagem": "/assets/dead-cells.png"
    },
    {
        "id": 8,
        "nome": "Hades",
        "ano": 2020,
        "genero": "Roguelike",
        "desenvolvedora": "Supergiant Games",
        "descricao": "Fuja do submundo em combates frenéticos.",
        "imagem": "/assets/hades.png"
    },
    {
        "id": 9,
        "nome": "Ori and the Blind Forest",
        "ano": 2015,
        "genero": "Metroidvania",
        "desenvolvedora": "Moon Studios",
        "descricao": "Aventura emocionante com visual impressionante.",
        "imagem": "/assets/ori.png"
    },
    {
        "id": 10,
        "nome": "The Binding of Isaac: Rebirth",
        "ano": 2014,
        "genero": "Roguelike",
        "desenvolvedora": "Nicalis",
        "descricao": "Masmorras aleatórias e centenas de itens.",
        "imagem": "/assets/isaac.png"
    }
]

@app.get("/")
def home():
    return {
        "mensagem": "API de Jogos Indies"
    }

@app.get("/jogos")
def listar_jogos():
    return jogos

@app.get("/jogos/{id}")
def buscar_jogo(id: int):
    for jogo in jogos:
        if jogo["id"] == id:
            return jogo

    raise HTTPException(
        status_code=404,
        detail="Jogo não encontrado"
    )

@app.get("/pesquisa")
def pesquisar(nome: str):
    resultado = []

    for jogo in jogos:
        if nome.lower() in jogo["nome"].lower():
            resultado.append(jogo)

    return resultado

@app.get("/quantidade")
def quantidade():
    return {
        "quantidade": len(jogos)
    }