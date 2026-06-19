fetch("http://127.0.0.1:8000/jogos")
    .then(res => res.json())
    .then(jogos => {

        const container = document.getElementById("jogos");

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

    })
    .catch(error => {
        console.error(error);
    });