from src.database.connection import orders_collection, menu_collection, waiter_collection
from datetime import datetime

class Item:
    @classmethod
    def add_item(cls, table_number: int, waiter_id: int, main_course: str = '', drink: str = '', starter: str = '', dessert: str = ''):
        main_course_data = None
        drink_data = None
        starter_data = None
        dessert_data = None

        if main_course:
            main_course_data = menu_collection.find_one({'name': main_course})
            if main_course_data is None:
                raise ValueError(f'{main_course} not found in menu.')

        if drink:
            drink_data = menu_collection.find_one({'name': drink})
            if drink_data is None:
                raise ValueError(f'{drink} not found in menu.')

        if starter:
            starter_data = menu_collection.find_one({'name': starter})
            if starter_data is None:
                raise ValueError(f'{starter} not found in menu.')
            
        if dessert:
            dessert_data = menu_collection.find_one({'name': dessert})
            if dessert_data is None:
                raise ValueError(f'{dessert} not found in menu.')

        waiter = waiter_collection.find_one({'waiter_id': waiter_id}, {'_id': 0})

        if waiter is None:
            raise ValueError(f'Waiter {waiter_id} not found.')

        table_order = orders_collection.find_one({
            'table_number': table_number,
        })

        
        new_item = {
            'item_id':           1 if table_order is None else len(table_order['items']) + 1,
            'main_course':       main_course,
            'main_course_price': main_course_data['price'] if main_course_data else 0,
            'drink':             drink,
            'drink_price':       drink_data['price']       if drink_data       else 0,
            'starter':           starter,
            'starter_price':     starter_data['price']     if starter_data     else 0,
            'dessert':           dessert,
            'dessert_price':     dessert_data['price']     if dessert_data     else 0
        }

        item_total = new_item['main_course_price'] + new_item['drink_price'] + new_item['starter_price'] + new_item['dessert_price']

        if table_order is None:
            orders_collection.insert_one({
                'table_number': table_number,
                'waiter_id': waiter_id,
                'creation_date': datetime.now().strftime('%d/%m/%Y'),
                'creation_time': datetime.now().strftime('%H:%M:%S'),
                'total_items': 1,
                'total_price': item_total,
                'items': [new_item]
            })
        else:
            orders_collection.update_one(
                {'table_number': table_number},
                {
                    '$push': {'items': new_item},
                    '$inc': {'total_items': 1, 'total_price': item_total}
                }
            )
            