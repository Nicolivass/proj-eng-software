const form = document.getElementById('form-restaurante');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const nome = document.getElementById('nome').value;
  const local = document.getElementById('local').value;
  const avaliacao = document.getElementById('avaliacao').value;

  try {
    const response = await fetch('http://127.0.0.1:5000/restaurantes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ nome, local, avaliacao }),
    });

    if (!response.ok) {
      const error = await response.json();
      alert(`Erro: ${error.erro}`);
      return;
    }

    alert('Restaurante cadastrado com sucesso!');
    form.reset();
  } catch (error) {
    alert('Erro ao cadastrar restaurante: ' + error.message);
  }
});