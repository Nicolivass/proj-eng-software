const form = document.getElementById('form-restaurante');

// Submeter formulário para criar ou editar
form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const id = form.dataset.id;
    const nome = document.getElementById('nome').value.trim();
    const local = document.getElementById('local').value.trim();
    const avaliacao = parseFloat(document.getElementById('avaliacao').value);

    if (!nome || !local || isNaN(avaliacao)) {
        alert("Por favor, preencha todos os campos corretamente.");
        return;
    }

    const url = id ? `http://127.0.0.1:5000/restaurantes/${id}` : "http://127.0.0.1:5000/restaurantes";
    const method = id ? 'PUT' : 'POST';

    try {
        const response = await fetch(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nome, local, avaliacao }),
        });

        if (response.ok) {
            alert(id ? "Restaurante atualizado com sucesso!" : "Restaurante cadastrado com sucesso!");
            form.reset(); 
            delete form.dataset.id; 
            window.location.href = 'restaurantes.html'; 
        } else {
            const error = await response.json();
            alert(error.erro || "Erro ao salvar restaurante.");
        }
    } catch (error) {
        console.error("Erro ao conectar ao servidor:", error);
        alert("Erro ao conectar ao servidor.");
    }
});

// Carregar os dados do restaurante
window.addEventListener('DOMContentLoaded', async () => {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');

    if (id) {
        try {
            const response = await fetch(`http://127.0.0.1:5000/restaurantes/${id}`);
            if (response.ok) {
                const restaurante = await response.json();

                document.getElementById('nome').value = restaurante.nome;
                document.getElementById('local').value = restaurante.local;
                document.getElementById('avaliacao').value = restaurante.avaliacao;
                document.getElementById('form-restaurante').dataset.id = id;
            } else {
                alert("Erro ao carregar os dados do restaurante.");
            }
        } catch (error) {
            console.error("Erro ao conectar ao servidor:", error);
        }
    }
});
