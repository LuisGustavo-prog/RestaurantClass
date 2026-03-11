from src.database.connection import orders_collection, menu_collection
from src.models.item import Item

class Order:
    def __init__(self, table_number: int, waiter_id: int, main_course: str = '', drink: str = '', starter: str = '', dessert: str =''):
        self._table_number = table_number
        self._waiter_id = waiter_id
        self._main_course = main_course
        self._drink = drink
        self._starter = starter
        self._dessert = dessert

        Order.post_order(
        table_number= self._table_number,
        waiter_id=self._waiter_id,
        main_course= self._main_course,
        drink= self._drink,
        starter= self._starter,
        dessert= self._dessert
    )

    @classmethod
    def post_order(cls, table_number: int, waiter_id, main_course: str = '', drink: str = '', starter: str = '', dessert: str = ''):
        Item.add_item(table_number= table_number, waiter_id=waiter_id, main_course= main_course, drink= drink, starter= starter, dessert= dessert)
        
    @classmethod
    def get_order(cls, table_number: int):        
        order = orders_collection.find_one({'table_number': table_number}, {'_id': 0})

        if order is None:
            return {'error': True, 'message': f'Table {table_number} not found.'}
        
        return order
    
    @classmethod
    def get_all_orders(cls):
        return list(orders_collection.find({}, {'_id': 0}))

    @classmethod
    def put_order(cls, table_number: int, item_id: int, new_main_course: str = '', new_drink: str = '', new_starter: str = '', new_dessert: str = ''):
        updated_fields = {}
    
        new_main_course_data = None
        new_drink_data = None
        new_starter_data = None
        new_dessert_data = None

        if new_main_course:
            new_main_course_data = menu_collection.find_one({'name': new_main_course})

            if new_main_course_data is None:
                raise ValueError(f'{new_main_course} not found in menu.')
            
            updated_fields['items.$.main_course'] = new_main_course
            updated_fields['items.$.main_course_price'] = new_main_course_data['price'] if new_main_course_data else 0

        if new_drink:
            new_drink_data = menu_collection.find_one({'name': new_drink})

            if new_drink_data is None:
                raise ValueError(f'{new_drink} not found in menu.')
            
            updated_fields['items.$.drink'] = new_drink
            updated_fields['items.$.drink_price'] = new_drink_data['price'] if new_drink_data else 0
            
        if new_starter:
            new_starter_data = menu_collection.find_one({'name': new_starter})

            if new_starter_data is None:
                raise ValueError(f'{new_starter} not found in menu.')
            
            updated_fields['items.$.starter'] = new_starter
            updated_fields['items.$.starter_price'] = new_starter_data['price'] if new_starter_data else 0
            
        if new_dessert:
            new_dessert_data = menu_collection.find_one({'name': new_dessert})

            if new_dessert_data is None:
                raise ValueError(f'{new_dessert} not found in menu.')

            updated_fields['items.$.dessert'] = new_dessert
            updated_fields['items.$.dessert_price'] = new_dessert_data['price'] if new_dessert_data else 0

        
        order = orders_collection.find_one({'table_number': table_number}, {'_id': 0})

        item = next((i for i in order['items'] if i['item_id'] == item_id), None)

        if order is None:
            return {'error': True, 'message': f'Table {table_number} not found.'}

        if item is None:
            return {'error': True, 'message': f'Item {item_id} not found.'}

        orders_collection.update_one({'table_number': table_number, 'items.item_id': item_id}, {
            '$set': updated_fields
        })

        order_update = orders_collection.find_one({'table_number': table_number})

        new_price = sum(
            item['main_course_price'] + item['drink_price'] + item['starter_price']
            for item in order_update['items']
        )

        orders_collection.update_one({'table_number': table_number}, {'$set': {'total_price': new_price}})

        return {'error': False, 'message': 'Order updated successfully!'}

    @classmethod
    def delete_order(cls, table_number: int):
        order = orders_collection.find_one({'table_number': table_number}, {'_id': 0})

        if order is None:
            return {'error': True, 'message': f'Table {table_number} not found.'}
        
        orders_collection.update_one(
            {'table_number': table_number},
            {'$set': {'items': [], 'total_items': 0, 'total_price': 0}}
        )

    @classmethod
    def delete_item(cls, table_number: int, item_id: int):
        order = orders_collection.find_one({'table_number': table_number}, {'_id': 0})

        if order is None:
            return {'error': True, 'message': f'Table {table_number} not found.'}
        
        item = next((data for data in order['items'] if data['item_id'] == item_id), None)

        if item is None:
            return {'error': True, 'message': f'Item {item_id} not found.'}
        
        orders_collection.update_one(
            {'table_number': table_number},
            {'$pull': {'items': {'item_id': item_id}}}
        )
