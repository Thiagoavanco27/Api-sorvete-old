from flask import Blueprint, jsonify, request, render_template, url_for, redirect
from .ice_cream_model import get_ice_cream_id, list_ice_creams, ice_cream_exists, add_ice_cream, delete_ice_cream, update_ice_cream, IceCreamNotFound

ice_creams_blueprint = Blueprint('ice_cream', __name__)

# Rota para obter todos os sorvetes
@ice_creams_blueprint.route('/ice_creams', methods=['GET'])
def get_ice_creams():
    ice_creams = list_ice_creams()
    return render_template("ice_cream.html", ice_creams=ice_creams)

# Rota para obter um sorvete pelo ID
@ice_creams_blueprint.route('/ice_creams/<int:ice_cream_id>', methods=['GET'])
def get_ice_cream(ice_cream_id):
    try:
        ice_cream = get_ice_cream_id(ice_cream_id)
        return render_template('ice_id.html', ice_cream=ice_cream)
    except IceCreamNotFound:
        return jsonify({'message': 'Sorvete não encontrado'}), 404

# Rota para acessar o formulário de criação de um novo sorvete
@ice_creams_blueprint.route('/ice_creams/add', methods=['GET'])
def add_ice_cream_page():
    return render_template('create_ice_cream.html')

# Rota para adicionar um novo sorvete
@ice_creams_blueprint.route('/ice_creams', methods=['POST'])
def post_ice_cream():
    data = request.json
    if 'flavor' not in data:
        return jsonify({'error': 'Sabor não encontrado'}), 400
    if ice_cream_exists(data.get('id')):
        return jsonify({'error': 'ID já utilizado'}), 400
    add_ice_cream(data)
    return jsonify(list_ice_creams())

# Rota para remover um sorvete pelo ID
@ice_creams_blueprint.route('/ice_creams/<int:ice_cream_id>', methods=['DELETE'])
def remove_ice_cream(ice_cream_id):
    try:
        delete_ice_cream(ice_cream_id)
        return "Removido!", 200
    except IceCreamNotFound:
        return jsonify({'message': 'Sorvete não encontrado'}), 404

# Rota para editar um sorvete pelo ID
@ice_creams_blueprint.route('/ice_creams/<int:ice_cream_id>', methods=['PUT'])
def edit_ice_cream(ice_cream_id):
    try:
        data = request.json
        if 'flavor' not in data:
            return jsonify({'error': 'Sabor do sorvete não encontrado'}), 400
        update_ice_cream(ice_cream_id, data)
        return redirect(url_for('ice_cream.get_ice_cream', ice_cream_id=ice_cream_id))
    except IceCreamNotFound:
        return jsonify({'message': 'Erro, sorvete não encontrado no sistema'}), 404

# Rota duplicada para deletar um sorvete (ajustada para evitar ambiguidade)
@ice_creams_blueprint.route('/ice_creams/delete/<int:ice_cream_id>', methods=['POST'])
def delete_ice_cream_route(ice_cream_id):
    try:
        delete_ice_cream(ice_cream_id)
        return redirect(url_for('ice_cream.get_ice_creams'))
    except IceCreamNotFound:
        return jsonify({'message': 'Erro, sorvete não encontrado no sistema'}), 404
