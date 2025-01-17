const restaurantes = [
    { nome: "Amarelinho N", local: "Norte", avaliacao: 4.5 },
    { nome: "Amarelinho S", local: "Sul", avaliacao: 4.5 },
    { nome: "Amarelinho C", local: "Centro", avaliacao: 4.5 },
    { nome: "RU", local: "Centro", avaliacao: 4.8 },
  ];
  
  const container = document.getElementById('restaurantes');
  
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