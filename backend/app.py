from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados fictícios
restaurantes = [
    {"id": 1, "nome": "Amarelinho N", "local": "Norte", "avaliacao": 4.5},
    {"id": 2, "nome": "Amarelinho S", "local": "Sul", "avaliacao": 4.5},
    {"id": 3, "nome": "Amarelinho C", "local": "Centro", "avaliacao": 4.5},
    {"id": 4, "nome": "RU", "local": "Centro", "avaliacao": 4.8},
]

# Rota para listar todos os restaurantes
@app.route('/restaurantes', methods=['GET'])
def get_restaurantes():
    return jsonify(restaurantes)

# Rota para buscar um restaurante pelo ID
@app.route('/restaurantes/<int:id>', methods=['GET'])
def get_restaurante(id):
    restaurante = next((r for r in restaurantes if r["id"] == id), None)
    if not restaurante:
        return jsonify({"erro": "Restaurante não encontrado"}), 404
    return jsonify(restaurante)

# Rota para adicionar restaurante
@app.route('/restaurantes', methods=['POST'])
def add_restaurante():
    if not request.is_json:
        return jsonify({"erro": "O conteúdo deve ser JSON"}), 400

    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"erro": f"Erro ao processar JSON: {str(e)}"}), 400

    if not all(key in data for key in ("nome", "local", "avaliacao")):
        return jsonify({"erro": "Dados inválidos, campos obrigatórios: nome, local, avaliacao"}), 400

    novo_restaurante = {
        "id": len(restaurantes) + 1,
        "nome": data["nome"],
        "local": data["local"],
        "avaliacao": float(data["avaliacao"]),
    }
    restaurantes.append(novo_restaurante)
    return jsonify(novo_restaurante), 201


# Rota para atualizar restaurante
@app.route('/restaurantes/<int:id>', methods=['PUT'])
def update_restaurante(id):
    if not request.is_json:
        return jsonify({"erro": "O conteúdo deve ser JSON"}), 400

    data = request.get_json()
    restaurante = next((r for r in restaurantes if r["id"] == id), None)
    if not restaurante:
        return jsonify({"erro": "Restaurante não encontrado"}), 404

    restaurante.update({
        "nome": data.get("nome", restaurante["nome"]),
        "local": data.get("local", restaurante["local"]),
        "avaliacao": float(data.get("avaliacao", restaurante["avaliacao"])),
    })
    return jsonify(restaurante)

# Rota para excluir restaurante
@app.route('/restaurantes/<int:id>', methods=['DELETE'])
def delete_restaurante(id):
    global restaurantes
    restaurante = next((r for r in restaurantes if r["id"] == id), None)
    if not restaurante:
        return jsonify({"erro": "Restaurante não encontrado"}), 404

    restaurantes = [r for r in restaurantes if r["id"] != id]
    return jsonify({"mensagem": "Restaurante excluído com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)