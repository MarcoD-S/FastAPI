fetch("http://127.0.0.1:8000/jogos")
    .then(res => res.json())
    .then(jogos => {

        const container = document.getElementById("jogos");

        jogos.forEach(jogo => {

            container.innerHTML += `
                <div class="card">
                    <h3>${jogo.nome}</h3>
                    <p>${jogo.descricao}</p>
                </div>
            `;

        });

    })
    .catch(error => {
        console.error(error);
    });