from src.entities.item import Item
from typing import Union

class Order:
    def __init__(self, table_number: int, main_course: str = None, drink: str = None, salad: str = None):
        self._table_number = table_number
        Order.post_order(table_number=table_number, main_course=main_course, drink=drink, salad=salad)

    @classmethod
    def post_order(cls, table_number: int, main_course: str = '', drink: str = '', salad: str = '') -> None:
        Item.add_item(table_number=table_number, main_course=main_course, drink=drink, salad=salad)
        
    @classmethod
    def get_order(cls, table: int = '', type_of_choice: str = 'all') -> Union[list[dict], dict]:
        pass

    @classmethod
    def put_order(cls, table: int, item_number: int, new_main_course: str = '', new_drink: str = '', new_salad: str = ''):
        pass

    @classmethod
    def delete_order(cls, table_number: int = None, item_number: int = None, type_of_choice: str = 'all'):
        pass
            