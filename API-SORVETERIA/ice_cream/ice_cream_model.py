from config import db

class IceCream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, flavor, category, price, stock_quantity):
        self.flavor = flavor
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
    
    def to_dict(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'category': self.category,
            'price': self.price,
            'stock_quantity': self.stock_quantity
        }

class IceCreamNotFound(Exception):
    pass

# Recupera um sorvete pelo seu ID
def get_ice_cream_id(ice_cream_id):
    ice_cream = IceCream.query.get(ice_cream_id)
    if not ice_cream:
        raise IceCreamNotFound
    return ice_cream.to_dict()

# Lista todos os sorvetes
def list_ice_creams():
    ice_creams = IceCream.query.all()
    return [ice_cream.to_dict() for ice_cream in ice_creams]

# Verifica se um sorvete existe pelo seu ID
def ice_cream_exists(ice_cream_id):
    try:
        get_ice_cream_id(ice_cream_id)
        return True
    except IceCreamNotFound:
        return False

# Adiciona um novo sorvete
def add_ice_cream(new_ice_cream):
    ice_cream = IceCream(
        flavor=new_ice_cream['flavor'],
        category=new_ice_cream['category'],
        price=new_ice_cream['price'],
        stock_quantity=new_ice_cream['stock_quantity']
    )
    db.session.add(ice_cream)
    db.session.commit()

# Deleta um sorvete pelo seu ID
def delete_ice_cream(ice_cream_id):
    ice_cream = IceCream.query.get(ice_cream_id)
    if not ice_cream:
        raise IceCreamNotFound
    db.session.delete(ice_cream)
    db.session.commit()

# Atualiza os detalhes de um sorvete pelo seu ID
def update_ice_cream(ice_cream_id, new_ice_cream):
    ice_cream = IceCream.query.get(ice_cream_id)
    if not ice_cream:
        raise IceCreamNotFound
    ice_cream.flavor = new_ice_cream['flavor']
    ice_cream.category = new_ice_cream['category']
    ice_cream.price = new_ice_cream['price']
    ice_cream.stock_quantity = new_ice_cream['stock_quantity']
    db.session.commit()
