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

    })
    .catch(error => {
        console.error(error);
    });

document
    .getElementById("pesquisa")
    .addEventListener("input", e => {

        const texto = e.target.value.toLowerCase();

        const filtrados = todosJogos.filter(jogo =>
            jogo.nome.toLowerCase().includes(texto)
        );

        renderizarJogos(filtrados);

    });