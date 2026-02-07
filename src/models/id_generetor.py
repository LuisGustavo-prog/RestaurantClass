class IDGenerato:
    IDGenerator = 0
    IDGenerato_Waiter = 0

    @classmethod
    def generate(cls):
        cls.IDGenerator += 1
        return cls.IDGenerator
    
    @classmethod
    def generate_waiter(cls):
        cls.IDGenerato_Waiter += 1
        return cls.IDGenerato_Waiter

    