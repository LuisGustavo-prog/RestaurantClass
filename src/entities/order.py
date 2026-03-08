from src.database.connection import orders_collection
from src.entities.item import Item
from typing import Union

class Order:
    def __init__(self, table_number: int, main_course: str = '', drink: str = '', starter: str = ''):
        self._table_number = table_number
        self._main_course = main_course
        self._drink = drink
        self._starter = starter

        Order.post_order(
        table_number= self._table_number,
        main_course= self._main_course,
        drink= self._drink,
        starter= self._starter
    )

    @classmethod
    def post_order(cls, table_number: int, main_course: str = '', drink: str = '', starter: str = '') -> None:
        Item.add_item(table_number= table_number, main_course= main_course, drink= drink, starter= starter)
        
    @classmethod
    def get_order(cls, table_number: int = None):
        if table_number is None:
            return list(orders_collection.find({}, {'_id': 0}))
        
        order = orders_collection.find_one({'table_number': table_number}, {'_id': 0})

        if order is None:
            return {'error': True, 'message': f'Mesa {table_number} não encontrada.'}
        
        return order

    @classmethod
    def put_order(cls, table_number: int, item_number: int, new_main_course: str = '', new_drink: str = '', new_starter: str = ''):
        pass

    @classmethod
    def delete_order(cls, table_number: int = None, item_number: int = None, type_of_choice: str = 'all'):
        pass
            