const API_URL = "http://127.0.0.1:5000/restaurantes"; // URL do backend
const container = document.getElementById('restaurantes');

// Função para listar restaurantes
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
                <button class="btn-editar" data-id="${restaurante.id}">Editar</button>
                <button class="btn-excluir" data-id="${restaurante.id}">Excluir</button>
            `;
            container.appendChild(card);
        });

        adicionarEventos();
    } catch (error) {
        console.error("Erro ao listar restaurantes:", error);
        container.innerHTML = '<p>Erro ao carregar restaurantes.</p>';
    }
}

// Função para preencher o formulário
function preencherFormularioEdicao(id) {
    window.location.href = `novo-restaurante.html?id=${id}`;
}

// Botão de editar
function adicionarEventos() {
    document.querySelectorAll('.btn-editar').forEach(button => {
        button.replaceWith(button.cloneNode(true));
    });

    document.querySelectorAll('.btn-editar').forEach(button => {
        button.addEventListener('click', (event) => {
            const id = event.target.dataset.id;
            preencherFormularioEdicao(id);
        });
    });

    document.querySelectorAll('.btn-excluir').forEach(button => {
        button.replaceWith(button.cloneNode(true)); // Evita eventos duplicados
    });

    document.querySelectorAll('.btn-excluir').forEach(button => {
        button.addEventListener('click', (event) => {
            const id = event.target.dataset.id;
            excluirRestaurante(id);
        });
    });
}

// Botão de excluir
async function excluirRestaurante(id) {
    if (!confirm("Tem certeza que deseja excluir este restaurante?")) return;

    try {
        const response = await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
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

// Chama listagem inicial
listarRestaurantes();