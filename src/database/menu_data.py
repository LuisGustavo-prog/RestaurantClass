from src.database.connection import menu_collection

menu_items = [
    # Main dishes
    {'name': 'Pizza Margherita',    'category': 'main_course', 'price': 39.90},
    {'name': 'Hamburguer',          'category': 'main_course', 'price': 29.90},
    {'name': 'Macarrão Bolonhesa',  'category': 'main_course', 'price': 34.90},

    # Entries
    {'name': 'Salada Caesar',       'category': 'starter',     'price': 19.90},
    {'name': 'Pão de Alho',         'category': 'starter',     'price': 12.90},

    # Drinks
    {'name': 'Coca-Cola',           'category': 'drink',       'price': 8.00},
    {'name': 'Suco de Laranja',     'category': 'drink',       'price': 10.00},
    {'name': 'Água',                'category': 'drink',       'price': 5.00},

    # Dessert
    {'name': 'Pudim',               'category': 'dessert',     'price': 14.90},
    {'name': 'Brownie',             'category': 'dessert',     'price': 16.90},
]

def populate_menu():
    if menu_collection.count_documents({}) == 0: 
        menu_collection.insert_many(menu_items)
        