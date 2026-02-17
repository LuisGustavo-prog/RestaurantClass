from src.entities.item import Item
from typing import Union

class Order:
    def __init__(self, table_number: int, main_course: str = None, drink: str = None, salad: str = None):
        self._table_number = table_number
        Order.post_order(table_number=table_number, main_course=main_course, drink=drink, salad=salad)
        
    def __str__(self) -> str:
        self_list = []

        for order in Item._order_list:
            if order['table_number'] == self._table_number:
                self_list.append(f'Mesa: {order['table_number']}, Id: {order['order_id']}')

                for item in order['items']:
                    self_list.append(f'  Item {item['item_number']}:')
                    self_list.append(f'    🍽️  Prato: {item['main_course']}')
                    self_list.append(f'    🥤 Bebida: {item['drink']}')
                    self_list.append(f'    🥗 Salada: {item['salad']}')

        return '\n'.join(self_list)
    
    @classmethod
    def post_order(cls, table_number: int, main_course: str = '', drink: str = '', salad: str = '') -> None:
        Item.add_item(table_number=table_number, main_course=main_course, drink=drink, salad=salad)

    @classmethod
    def get_order_terminal(cls, table: int = '', type_of_choice: str = 'all') -> str:
        result_get = []
        validation = ('all', 'specific')
        data = Item._order_list # Armazena a referência da lista.

        if type_of_choice not in validation:
            return f'❌ Opção inválida.\n Opções disponíveis: {', '.join(validation)}'
        
        if type_of_choice == 'all' and table == '':
            for order in data:
                result_get.append(f'Mesa: {order['table_number']}, Id: {order['order_id']}')
    
                for item in order['items']:
                    result_get.append(f'  Item {item['item_number']}:')
                    result_get.append(f'    🍽️  Prato: {item['main_course']}')
                    result_get.append(f'    🥤 Bebida: {item['drink']}')
                    result_get.append(f'    🥗 Salada: {item['salad']}\n')

        if type_of_choice == 'specific' and isinstance(table, int):
            for order in data:
                if order['table_number'] == table:
                    result_get.append(f'Mesa: {order['table_number']}, Id: {order['order_id']}')

                    for item in order['items']:
                        result_get.append(f'  Item {item['item_number']}:')
                        result_get.append(f'    🍽️  Prato: {item['main_course']}')
                        result_get.append(f'    🥤 Bebida: {item['drink']}')
                        result_get.append(f'    🥗 Salada: {item['salad']}')

        return '\n'.join(result_get)
        
    @classmethod
    def get_order(cls, table: int = '', type_of_choice: str = 'all') -> Union[list[dict], dict]:
        validation = ('all', 'specific') 
        data = Item._order_list

        if type_of_choice not in validation:
            return {
                'error': True,
                'message': f'Opção inválida. Opções disponíveis: {', '.join(validation)}'
            }

        if type_of_choice == 'all':
            return data
        
        if type_of_choice == 'specific':
            for order in data:
                if table == order['table_number']:
                    return order
            
            return {
                'error': True,
                'message': f'Mesa {table} não encontrada.'
            }
        
        return {
            'error': True,
            'message': 'Parâmetros inválidos.'
        }        

    @classmethod
    def put_order(cls, table: int, item_number: int, new_main_course: str = '', new_drink: str = '', new_salad: str = '') -> str:
        data = Item._order_list
        
        if not any(order['table_number'] == table for order in data):
            return {
                'error': True,
                'message': f'Mesa {table} não encontrada.'
            }
        
        for order in data:
            if order['table_number'] == table:
                
                for item in order['items']:
                    if item['item_number'] == item_number:
                        item['main_course'] = new_main_course if new_main_course != '' else None
                        item['drink'] = new_drink if new_drink != '' else None
                        item['salad'] = new_salad if new_salad != '' else None

                        return {
                            'error': False,
                            'message': 'Pedido atualizado com sucesso!'
                        }
                
                return {
                    'error': True,
                    'message': f'Item {item_number} não encontrado na mesa {table}.'
                }
            
    @classmethod
    def delete_order(cls, table_number: int = None, item_number: int = None, type_of_choice: str = 'all') -> str:
        validation = ('all', 'specific')
        data = Item._order_list

        if type_of_choice not in validation:
            return {
                'error': True,
                'message': f'Opção inválida. Opções disponíveis: {', '.join(validation)}'
            }
        
        if type_of_choice == 'all':
            data.clear()

            return {
                'error': False,
                'message': 'Comandas apagadas.'
            }
        
        if type_of_choice == 'specific':
            for order in data:
                if table_number == order['table_number']:
                    for item in order['items']:
                        if item_number == item['item_number']:
                            order['items'].remove(item)
                            
                            return {
                                'error': False,
                                'message': 'Item apagado.'
                            }
                        
                        return {
                            'error': True,
                            'message': f'Pedido de número {item_number} não encotrado.'
                        }

                return {
                    'error': True,
                    'message': f'Mesa de número {table_number} não encontrada.'
                }
        
        return {
            'error': True,
            'message': 'Parâmetros inválidos.'
        }
            