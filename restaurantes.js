const container = document.getElementById('restaurantes');

async function carregarRestaurantes() {
  try {
    const response = await fetch('http://127.0.0.1:5000/restaurantes');
    if (!response.ok) {
      throw new Error('Erro ao carregar restaurantes');
    }

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
    container.innerHTML = '<p>Erro ao carregar restaurantes.</p>';
  }
}

carregarRestaurantes();