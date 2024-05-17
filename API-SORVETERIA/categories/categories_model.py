from config import db

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String, nullable=False)

    def __init__(self, category_name):
        self.category_name = category_name
    
    def to_dict(self):
        return {'id': self.id, 'category_name': self.category_name}

class CategoryNotFound(Exception):
    pass

# Recupera uma categoria pelo seu ID
def get_category_id(category_id):
    category = Categories.query.get(category_id)
    if not category:
        raise CategoryNotFound
    return category.to_dict()

# Lista todas as categorias
def categories_list():
    categories = Categories.query.all()
    return [category.to_dict() for category in categories]

# Verifica se uma categoria existe pelo seu ID
def category_exists(category_id):
    try:
        get_category_id(category_id)
        return True
    except CategoryNotFound:
        return False

# Adiciona uma nova categoria
def add_category(new_category):
    category = Categories(category_name=new_category['category_name'])
    db.session.add(category)
    db.session.commit()

# Deleta uma categoria pelo seu ID
def delete_category(category_id):
    category = Categories.query.get(category_id)
    if not category:
        raise CategoryNotFound
    db.session.delete(category)
    db.session.commit()

# Atualiza o nome de uma categoria pelo seu ID
def update_category(category_id, new_category):
    category = Categories.query.get(category_id)
    if not category:
        raise CategoryNotFound
    category.category_name = new_category['category_name']
    db.session.commit()
