from src.database.connection import menu_collection

class Menu:
    @classmethod
    def get_menu(cls):
        return list(menu_collection.find({}, {'_id': 0}))
    
    @classmethod
    def get_by_category(cls, category: str):
        return list(menu_collection.find({'category': category}, {'_id': 0}))
    
    @classmethod
    def get_by_name(cls, name: str):
        return list(menu_collection.find({'name': name}, {'_id': 0}))
    
