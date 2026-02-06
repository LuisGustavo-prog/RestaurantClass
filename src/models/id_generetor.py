class IDGenerato:
    IDGenerator = 0

    @classmethod
    def generate(cls):
        cls.IDGenerator += 1
        return cls.IDGenerator
    