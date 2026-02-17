from src.entities.id_generetor import IDGenerato
from datetime import datetime

class Item:
    _order_list = []
    
    @classmethod
    def add_item(cls, table_number: int, order_id: int = '', main_course: str = '', drink: str = '', salad: str = '') -> None:
        if order_id == '':
            order_id = IDGenerato.get_or_create_order_id(table_number=table_number)
    
        new_item = {
            'item_number': 1,
            'main_course': main_course,
            'drink': drink,
            'salad': salad
        }

        table_order = None
        for order in cls._order_list:
            if order['table_number'] == table_number and order['order_id'] == order_id:
                table_order = order # Armazenando a referência da lista.
                break

        if table_order is None:
            cls._order_list.append({
                'table_number': table_number,
                'order_id': order_id,
                'creation_date': datetime.now().strftime('%d/%m/%Y'),
                'creation_time': datetime.now().strftime('%H:%M:%S'),
                'items': [new_item]
            })
        else:
            new_item['item_number'] = len(table_order['items']) + 1  
            table_order['items'].append(new_item)
        