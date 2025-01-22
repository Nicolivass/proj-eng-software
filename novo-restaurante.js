const API_URL = "http://127.0.0.1:5000";
const formRestaurante = document.getElementById("form-restaurante");
const menuContainer = document.getElementById("menu-container");
const adicionarMenuButton = document.getElementById("adicionar-menu");

const urlParams = new URLSearchParams(window.location.search);
const restauranteId = urlParams.get('id');

if (restauranteId) {
  carregarRestauranteParaEdicao(restauranteId);
}

async function carregarRestauranteParaEdicao(id) {
  try {
    const response = await fetch(`${API_URL}/restaurantes/${id}`);
    const restaurante = await response.json();

    if (!restaurante) {
      alert("Restaurante não encontrado.");
      return;
    }

    document.getElementById("nome").value = restaurante.nome;
    document.getElementById("local").value = restaurante.local;
    document.getElementById("avaliacao").value = restaurante.avaliacao;

    menuContainer.innerHTML = '';

    if (restaurante.menus && restaurante.menus.length > 0) {
      restaurante.menus.forEach(menu => {
        adicionarMenu(menu.nome, menu.preco); 
      });
    }
  } catch (error) {
    console.error("Erro ao carregar dados do restaurante:", error);
    alert("Erro ao carregar restaurante para edição.");
  }
}

function adicionarMenu(nome = '', preco = '') {
  const menuId = `menu-${Date.now()}`;  
  
  const menuDiv = document.createElement("div");
  menuDiv.classList.add("menu-item");
  
  menuDiv.innerHTML = `
    <label for="${menuId}-nome">Nome do Menu:</label>
    <input type="text" id="${menuId}-nome" name="menus[nome]" value="${nome}" required>
    
    <label for="${menuId}-preco">Preço:</label>
    <input type="number" id="${menuId}-preco" name="menus[preco]" value="${preco}" step="0.01" required>
    
    <button type="button" class="remover-menu">Remover</button>
  `;
  
  menuContainer.appendChild(menuDiv);

  menuDiv.querySelector(".remover-menu").addEventListener("click", () => {
    menuContainer.removeChild(menuDiv);
  });
}

async function salvarRestaurante(event) {
  event.preventDefault();

  const formData = new FormData(formRestaurante);
  const data = {
    nome: formData.get("nome"),
    local: formData.get("local"),
    avaliacao: parseFloat(formData.get("avaliacao")),
    menus: []
  };

  const menus = formData.getAll("menus[nome]");
  const precos = formData.getAll("menus[preco]");

  if (menus.length === precos.length) {
    for (let i = 0; i < menus.length; i++) {
      const nome = menus[i];
      const preco = parseFloat(precos[i]);
      if (nome && preco) {
        data.menus.push({ nome, preco });
      }
    }
  } else {
    alert("Por favor, preencha todos os campos de menu.");
    return;
  }

  try {
    let response;

    if (restauranteId) {
      response = await fetch(`${API_URL}/restaurantes/${restauranteId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
    } else {
      response = await fetch(`${API_URL}/restaurantes`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
    }

    if (response.ok) {
      alert(restauranteId ? "Restaurante editado com sucesso!" : "Restaurante cadastrado com sucesso!");
      formRestaurante.reset();
      if (restauranteId) {
        window.location.href = "restaurantes.html";
      }
    } else {
      const error = await response.json();
      alert(error.erro || "Erro ao salvar restaurante.");
    }
  } catch (error) {
    console.error("Erro ao salvar restaurante:", error);
    alert("Erro ao conectar ao servidor.");
  }
}

adicionarMenuButton.addEventListener("click", () => adicionarMenu());
formRestaurante.addEventListener("submit", salvarRestaurante);