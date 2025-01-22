const API_URL = "http://127.0.0.1:5000";
const container = document.getElementById("restaurantes");

async function listarRestaurantes() {
  try {
    const response = await fetch(`${API_URL}/restaurantes`);
    const restaurantes = await response.json();

    container.innerHTML = "";

    restaurantes.forEach((restaurante) => {
      const card = document.createElement("div");
      card.classList.add("restaurante-card");

      card.innerHTML = `
        <h3>${restaurante.nome}</h3>
        <p>Local: ${restaurante.local}</p>
        <p>Avaliação: ${restaurante.avaliacao}</p>
        <button class="btn-ver-menus" data-id="${restaurante.id}">Ver Menus</button>
        <button class="btn-editar" data-id="${restaurante.id}">Editar</button>
        <button class="btn-excluir" data-id="${restaurante.id}">Excluir</button>
      `;

      container.appendChild(card);
    });

    adicionarEventos();
  } catch (error) {
    console.error("Erro ao listar restaurantes:", error);
    container.innerHTML = "<p>Erro ao carregar restaurantes.</p>";
  }
}

async function listarMenus(restauranteId) {
  try {
    const response = await fetch(`${API_URL}/restaurantes/${restauranteId}/menus`);
    const menus = await response.json();

    if (!response.ok || menus.erro) {
      alert(menus.erro || "Erro ao carregar menus.");
      return;
    }

    const modalContent = document.getElementById("menu-content");
    modalContent.innerHTML = menus
      .map((menu) => `<p>${menu.nome} - R$${menu.preco.toFixed(2)}</p>`)
      .join("");
    document.getElementById("menu-modal").classList.add("visible");
  } catch (error) {
    console.error("Erro ao listar menus:", error);
    alert("Erro ao conectar ao servidor.");
  }
}

document.getElementById("menu-modal-close").addEventListener("click", () => {
  document.getElementById("menu-modal").classList.remove("visible");
});

function preencherFormularioEdicao(id) {
  window.location.href = `novo-restaurante.html?id=${id}`;
}
function adicionarEventos() {
  document.querySelectorAll('.btn-ver-menus').forEach(button => {
    button.addEventListener('click', (event) => {
      const id = event.target.dataset.id;
      listarMenus(id);
    });
  });

  document.querySelectorAll('.btn-editar').forEach(button => {
    button.addEventListener('click', (event) => {
      const id = event.target.dataset.id;
      preencherFormularioEdicao(id);
    });
  });

  document.querySelectorAll('.btn-excluir').forEach(button => {
    button.addEventListener('click', (event) => {
      const id = event.target.dataset.id;
      excluirRestaurante(id);
    });
  });
}

async function excluirRestaurante(id) {
  if (!confirm("Tem certeza que deseja excluir este restaurante?")) return;

  try {
    const response = await fetch(`${API_URL}/restaurantes/${id}`, { method: 'DELETE' });
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