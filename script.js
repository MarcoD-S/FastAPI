let todosJogos = [];

const botaoLayout = document.getElementById("trocarLayout");
const container = document.getElementById("jogos");

botaoLayout.addEventListener("click", () => {

    container.classList.toggle("lista");

    if(container.classList.contains("lista")){
        botaoLayout.textContent = "🔲 Grade";
    }else{
        botaoLayout.textContent = "📋 Lista";
    }

});

function renderizarJogos(jogos){

    container.innerHTML = "";

    jogos.forEach(jogo => {

        container.innerHTML += `
            <div class="card">

                <img
                    src="http://127.0.0.1:8000${jogo.imagem}"
                    alt="${jogo.nome}"
                >

                <div class="card-content">

                    <h3>${jogo.nome}</h3>

                    <div class="info">
                        <span>🎮 ${jogo.genero}</span>
                        <span>📅 ${jogo.ano}</span>
                        <span>⭐ ${jogo.nota ?? "N/A"}</span>
                    </div>

                    <p class="dev">
                        Desenvolvedora: ${jogo.desenvolvedora}
                    </p>

                    <p class="descricao">
                        ${jogo.descricao}
                    </p>

                </div>

            </div>
        `;
    });
}

fetch("http://127.0.0.1:8000/jogos")
    .then(res => res.json())
    .then(jogos => {

        todosJogos = jogos;

        renderizarJogos(jogos);

        destaques = jogos.slice(0, 5);

        atualizarHero();

        setInterval(() => {

            destaqueAtual++;

            if(destaqueAtual >= destaques.length){
                destaqueAtual = 0;
            }

            atualizarHero();

        }, 5000);

    })
    .catch(error => {
        console.error(error);
    });

const hero = document.getElementById("hero");
const heroTitulo = document.getElementById("heroTitulo");
const heroDescricao = document.getElementById("heroDescricao");

let destaqueAtual = 0;
let destaques = [];

function atualizarHero(){

    const jogo = destaques[destaqueAtual];

    hero.style.backgroundImage =
    `url(http://127.0.0.1:8000${jogo.banner})`;

    heroTitulo.textContent = jogo.nome;

    heroDescricao.textContent = jogo.descricao;
}
atualizarHero();

setInterval(() => {

    destaqueAtual++;

    if(destaqueAtual >= destaques.length){
        destaqueAtual = 0;
    }

    atualizarHero();

}, 5000);