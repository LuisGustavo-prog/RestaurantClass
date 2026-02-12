class IDGenerato:
    IDGenerator = 0
    IDGenerato_Waiter = 0

    _table_order_ids = {}
    _waiters_ids = {}

    @classmethod
    def generate(cls):
        cls.IDGenerator += 1
        return cls.IDGenerator
    
    @classmethod
    def generate_waiter(cls):
        cls.IDGenerato_Waiter += 1
        return cls.IDGenerato_Waiter
    
    @classmethod
    def get_or_create_order_id(cls, table_number: int) -> int:  
        if table_number not in cls._table_order_ids: 
            new_id = cls.generate()

            cls._table_order_ids[table_number] = new_id 

        return cls._table_order_ids[table_number]
    
    @classmethod
    def get_or_create_waiter_id(cls, name) -> int:
        if name not in cls._waiters_ids:
            new_id = cls.generate_waiter()
        
            cls._waiters_ids[name] = new_id
        
        return cls._waiters_ids[name]
 