from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

restaurantes = [
    {"id": 1, "nome": "Amarelinho N", "local": "Norte", "avaliacao": 4.5},
    {"id": 2, "nome": "Amarelinho S", "local": "Sul", "avaliacao": 4.5},
    {"id": 3, "nome": "Amarelinho C", "local": "Centro", "avaliacao": 4.5},
    {"id": 4, "nome": "RU", "local": "Centro", "avaliacao": 4.8},
]

menus = [
    {"id": 1, "restaurante_id": 1, "nome": "Prato Executivo", "preco": 25.00},
    {"id": 2, "restaurante_id": 1, "nome": "Suco Natural", "preco": 8.00},
    {"id": 3, "restaurante_id": 2, "nome": "Pizza Marguerita", "preco": 30.00},
]

@app.route('/restaurantes', methods=['GET'])
def get_restaurantes():
    return jsonify(restaurantes)

@app.route('/restaurantes/<int:id>', methods=['GET'])
def get_restaurante(id):
    restaurante = next((r for r in restaurantes if r["id"] == id), None)
    if not restaurante:
        return jsonify({"erro": "Restaurante não encontrado"}), 404
    return jsonify(restaurante)

@app.route('/restaurantes', methods=['POST'])
def add_restaurante():
    if not request.is_json:
        return jsonify({"erro": "O conteúdo deve ser JSON"}), 400

    data = request.get_json()
    if not all(key in data for key in ("nome", "local", "avaliacao")):
        return jsonify({"erro": "Dados do restaurante incompletos"}), 400

    novo_restaurante = {
        "id": len(restaurantes) + 1,
        "nome": data["nome"],
        "local": data["local"],
        "avaliacao": data["avaliacao"],
    }
    restaurantes.append(novo_restaurante)

    if "menus" in data and isinstance(data["menus"], list):
        for menu in data["menus"]:
            if not all(key in menu for key in ("nome", "preco")):
                continue
            novo_menu = {
                "id": len(menus) + 1,
                "restaurante_id": novo_restaurante["id"],
                "nome": menu["nome"],
                "preco": menu["preco"],
            }
            menus.append(novo_menu)

    return jsonify(novo_restaurante), 201

@app.route('/restaurantes/<int:id>', methods=['PUT'])
def update_restaurante(id):
    data = request.get_json()
    if not all(key in data for key in ("nome", "local", "avaliacao")):
        return jsonify({"erro": "Dados do restaurante incompletos"}), 400

    restaurante = next((r for r in restaurantes if r['id'] == id), None)
    if not restaurante:
        return jsonify({"erro": "Restaurante não encontrado"}), 404

    restaurante.update({
        "nome": data["nome"],
        "local": data["local"],
        "avaliacao": data["avaliacao"]
    })

    if "menus" in data and isinstance(data["menus"], list):
        global menus
        menus = [m for m in menus if m["restaurante_id"] != id]

        for menu in data["menus"]:
            if not all(key in menu for key in ("nome", "preco")):
                continue
            novo_menu = {
                "id": len(menus) + 1,
                "restaurante_id": id,
                "nome": menu["nome"],
                "preco": menu["preco"],
            }
            menus.append(novo_menu)

    return jsonify(restaurante), 200

@app.route('/restaurantes/<int:restaurante_id>/menus', methods=['GET'])
def get_menus_by_restaurante(restaurante_id):
    restaurante_menus = [menu for menu in menus if menu["restaurante_id"] == restaurante_id]
    if not restaurante_menus:
        return jsonify({"erro": "Nenhum menu encontrado para este restaurante."}), 404
    return jsonify(restaurante_menus)

@app.route('/menus', methods=['GET'])
def get_all_menus():
    return jsonify(menus)

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