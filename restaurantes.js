// Função para buscar e exibir restaurantes
async function listarRestaurantes() {
    try {
        const response = await fetch("http://127.0.0.1:5000/restaurantes");
        const restaurantes = await response.json();

        const container = document.getElementById('restaurantes');
        container.innerHTML = '';

        restaurantes.forEach(restaurante => {
            const card = document.createElement('div');
            card.className = 'restaurante-card';
            card.innerHTML = `
                <h3>${restaurante.nome}</h3>
                <p>Local: ${restaurante.local}</p>
                <p>Avaliação: ${restaurante.avaliacao}</p>
                <button class="btn-excluir" data-id="${restaurante.id}">Excluir</button>
            `;
            container.appendChild(card);
        });

        document.querySelectorAll('.btn-excluir').forEach(button => {
            button.addEventListener('click', (event) => {
                const id = event.target.dataset.id;
                excluirRestaurante(id);
            });
        });
    } catch (error) {
        console.error("Erro ao carregar restaurantes:", error);
    }
}

// Função para excluir restaurante
async function excluirRestaurante(id) {
    if (!confirm("Tem certeza que deseja excluir este restaurante?")) return;

    try {
        const response = await fetch(`http://127.0.0.1:5000/restaurantes/${id}`, {
            method: 'DELETE',
        });

        if (response.ok) {
            alert("Restaurante excluído com sucesso!");
            listarRestaurantes();
        } else {
            alert("Erro ao excluir restaurante.");
        }
    } catch (error) {
        console.error("Erro ao excluir restaurante:", error);
        alert("Erro ao conectar ao servidor.");
    }
}

listarRestaurantes();