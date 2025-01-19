const API_URL = "http://127.0.0.1:5000/restaurantes";
const form = document.getElementById('form-restaurante');

// Função para enviar dados do formulário
form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const local = document.getElementById('local').value;
    const avaliacao = document.getElementById('avaliacao').value;

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nome, local, avaliacao }),
        });

        if (response.ok) {
            alert("Restaurante cadastrado com sucesso!");
            form.reset();
        } else {
            alert("Erro ao cadastrar restaurante.");
        }
    } catch (error) {
        console.error("Erro ao enviar restaurante:", error);
        alert("Erro ao conectar ao servidor.");
    }
});