const form = document.getElementById('form-restaurante');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const nome = document.getElementById('nome').value;
  const local = document.getElementById('local').value;
  const avaliacao = document.getElementById('avaliacao').value;

  alert(`Restaurante cadastrado:\nNome: ${nome}\nLocal: ${local}\nAvaliação: ${avaliacao}`);

  form.reset();
});