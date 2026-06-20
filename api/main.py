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
        "imagem": "/assets/undertale.png",
        "banner": "/assets/banners/undertale-banner.png"
    },
    {
        "id": 2,
        "nome": "Hollow Knight",
        "ano": 2017,
        "genero": "Metroidvania",
        "desenvolvedora": "Team Cherry",
        "descricao": "Exploração, combate desafiador e um vasto reino subterrâneo.",
        "imagem": "/assets/hollow-knight.png",
        "banner": "/assets/banners/hollow-knight-banner.png"
    },
    {
        "id": 3,
        "nome": "Celeste",
        "ano": 2018,
        "genero": "Plataforma",
        "desenvolvedora": "Maddy Makes Games",
        "descricao": "Plataforma precisa com narrativa emocionante.",
        "imagem": "/assets/celeste.png",
        "banner": "/assets/banners/celeste-banner.png"
    },
    {
        "id": 4,
        "nome": "Stardew Valley",
        "ano": 2016,
        "genero": "Simulação",
        "desenvolvedora": "ConcernedApe",
        "descricao": "Gerencie uma fazenda e construa relacionamentos.",
        "imagem": "/assets/stardew-valley.png",
        "banner": "/assets/banners/stardew-valley-banner.png"
    },
    {
        "id": 5,
        "nome": "Terraria",
        "ano": 2011,
        "genero": "Sandbox",
        "desenvolvedora": "Re-Logic",
        "descricao": "Exploração, construção e combate em mundo 2D.",
        "imagem": "/assets/terraria.png",
        "banner": "/assets/banners/terraria-banner.png"
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
    },
    {
        "id": 11,
        "nome": "Slay the Spire",
        "ano": 2019,
        "genero": "Roguelike Deckbuilder",
        "desenvolvedora": "Mega Crit",
        "nota": 9.3,
        "descricao": "Mistura estratégia de cartas com elementos roguelike em partidas altamente rejogáveis.",
        "imagem": "/assets/slay-the-spire.png"
    },
    {
        "id": 12,
        "nome": "Inscryption",
        "ano": 2021,
        "genero": "Card Game",
        "desenvolvedora": "Daniel Mullins Games",
        "nota": 9.4,
        "descricao": "Jogo de cartas com elementos de terror psicológico e mistérios.",
        "imagem": "/assets/inscryption.png"
    },
    {
        "id": 13,
        "nome": "Outer Wilds",
        "ano": 2019,
        "genero": "Exploração",
        "desenvolvedora": "Mobius Digital",
        "nota": 9.8,
        "descricao": "Explore um sistema solar preso em um ciclo temporal e descubra seus segredos.",
        "imagem": "/assets/outer-wilds.png"
    },
    {
        "id": 14,
        "nome": "A Short Hike",
        "ano": 2019,
        "genero": "Aventura",
        "desenvolvedora": "Adam Robinson-Yu",
        "nota": 9.0,
        "descricao": "Uma aventura relaxante explorando uma montanha e seus arredores.",
        "imagem": "/assets/a-short-hike.png"
    },
    {
        "id": 15,
        "nome": "Katana ZERO",
        "ano": 2019,
        "genero": "Ação",
        "desenvolvedora": "Askiisoft",
        "nota": 9.2,
        "descricao": "Ação frenética com manipulação do tempo e narrativa envolvente.",
        "imagem": "/assets/katana-zero.png"
    },
    {
        "id": 16,
        "nome": "Hyper Light Drifter",
        "ano": 2016,
        "genero": "Ação RPG",
        "desenvolvedora": "Heart Machine",
        "nota": 9.1,
        "descricao": "Exploração e combate em um mundo misterioso inspirado em clássicos 16-bit.",
        "imagem": "/assets/hyper-light-drifter.png"
    },
    {
        "id": 17,
        "nome": "Shovel Knight",
        "ano": 2014,
        "genero": "Plataforma",
        "desenvolvedora": "Yacht Club Games",
        "nota": 9.2,
        "descricao": "Plataforma retrô inspirada nos clássicos do NES.",
        "imagem": "/assets/shovel-knight.png"
    },
    {
        "id": 18,
        "nome": "Blasphemous",
        "ano": 2019,
        "genero": "Metroidvania",
        "desenvolvedora": "The Game Kitchen",
        "nota": 8.9,
        "descricao": "Metroidvania sombrio inspirado no folclore e arte religiosa espanhola.",
        "imagem": "/assets/blasphemous.png"
    },
    {
        "id": 19,
        "nome": "Spiritfarer",
        "ano": 2020,
        "genero": "Simulação",
        "desenvolvedora": "Thunder Lotus Games",
        "nota": 9.1,
        "descricao": "Gerencie uma embarcação e ajude espíritos em sua jornada final.",
        "imagem": "/assets/spiritfarer.png"
    },
    {
        "id": 20,
        "nome": "Dave the Diver",
        "ano": 2023,
        "genero": "Aventura",
        "desenvolvedora": "Mintrocket",
        "nota": 9.0,
        "descricao": "Pesque durante o dia e administre um restaurante de sushi à noite.",
        "imagem": "/assets/dave-the-diver.png"
    },
    {
        "id": 21,
        "nome": "Pizza Tower",
        "ano": 2023,
        "genero": "Plataforma",
        "desenvolvedora": "Tour De Pizza",
        "nota": 9.4,
        "descricao": "Plataforma frenética inspirada na série Wario Land.",
        "imagem": "/assets/pizza-tower.png"
    },
    {
        "id": 22,
        "nome": "Animal Well",
        "ano": 2024,
        "genero": "Metroidvania",
        "desenvolvedora": "Shared Memory",
        "nota": 9.2,
        "descricao": "Exploração não linear cheia de segredos e quebra-cabeças.",
        "imagem": "/assets/animal-well.png"
    },
    {
        "id": 23,
        "nome": "Balatro",
        "ano": 2024,
        "genero": "Roguelike Deckbuilder",
        "desenvolvedora": "LocalThunk",
        "nota": 9.6,
        "descricao": "Mistura pôquer com mecânicas roguelike extremamente viciantes.",
        "imagem": "/assets/balatro.png"
    },
    {
        "id": 24,
        "nome": "OMORI",
        "ano": 2020,
        "genero": "RPG",
        "desenvolvedora": "OMOCAT",
        "nota": 9.5,
        "descricao": "RPG psicológico com narrativa emocional e visual marcante.",
        "imagem": "/assets/omori.png"
    },
    {
        "id": 25,
        "nome": "Rain World",
        "ano": 2017,
        "genero": "Sobrevivência",
        "desenvolvedora": "Videocult",
        "nota": 9.0,
        "descricao": "Sobreviva em um ecossistema hostil controlando um slugcat.",
        "imagem": "/assets/rain-world.png"
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