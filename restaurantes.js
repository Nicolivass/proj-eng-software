const API_URL = "http://127.0.0.1:5000/restaurantes";
const container = document.getElementById('restaurantes');

// Função para buscar e exibir restaurantes
async function listarRestaurantes() {
    try {
        const response = await fetch(API_URL);
        const restaurantes = await response.json();

        container.innerHTML = '';

        restaurantes.forEach(restaurante => {
            const card = document.createElement('div');
            card.className = 'restaurante-card';
            card.innerHTML = `
                <h3>${restaurante.nome}</h3>
                <p>Local: ${restaurante.local}</p>
                <p>Avaliação: ${restaurante.avaliacao}</p>
            `;
            container.appendChild(card);
        });
    } catch (error) {
        console.error("Erro ao listar restaurantes:", error);
        container.innerHTML = '<p>Erro ao carregar restaurantes.</p>';
    }
}

listarRestaurantes();