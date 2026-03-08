from src.utils.id_generator import generate_waiter_id
from datetime import datetime
from src.utils.validators import cpf_validator, name_validator, email_validator, phone_number_validator
from src.database.connection import waiter_collection

class Waiter:
    def __init__(self, name: str, cpf: str, wage: float, email: str, phone_number: str):
        self._waiter_id = generate_waiter_id()       
        self._name = name_validator(name=name)                 
        self._cpf = cpf_validator(cpf=cpf) 
        self._wage = wage                
        self._email = email_validator(email=email)                 
        self._phone_number = phone_number_validator(phone_number=phone_number)                
        self._hire_date = datetime.now().date()          
        self.register()

    def register(self):
        waiter_collection.insert_one({
            'waiter_id':    self._waiter_id,
            'name':         self._name,
            'cpf':          self._cpf,
            'wage':         self._wage,
            'email':        self._email,
            'phone_number': self._phone_number,
            'hire_date':    str(self._hire_date)
        })
        
    
    