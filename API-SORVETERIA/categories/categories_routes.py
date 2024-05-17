from flask import Blueprint, jsonify, request, redirect, url_for
from .categories_model import get_category_id, categories_list, category_exists, add_category, delete_category, update_category, CategoryNotFound

categories_blueprint = Blueprint('categories', __name__)

# Rota para obter todas as categorias
@categories_blueprint.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories_list())

# Rota para adicionar uma nova categoria
@categories_blueprint.route('/categories', methods=['POST'])
def post_category():
    data = request.json
    if 'category_name' not in data:
        return jsonify({'error': 'Nome da categoria não encontrado'}), 400
    if category_exists(data.get('id')):
        return jsonify({'error': 'ID já utilizado'}), 400
    add_category(data)
    return jsonify(categories_list())

# Rota para remover uma categoria pelo ID
@categories_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
def remove_category(category_id):
    try:
        delete_category(category_id)
        return "Removido!", 200
    except CategoryNotFound:
        return jsonify({'message': 'Erro, categoria não encontrada no sistema'}), 404

# Rota para editar uma categoria pelo ID
@categories_blueprint.route('/categories/<int:category_id>', methods=['PUT'])
def edit_category(category_id):
    try:
        data = request.json
        if 'category_name' not in data:
            return jsonify({'error': 'Nome da categoria não encontrado'}), 400
        update_category(category_id, data)
        return redirect(url_for('categories.get_categories'))
    except CategoryNotFound:
        return jsonify({'message': 'Erro, categoria não encontrada no sistema'}), 404
