from src.utils.id_generator import generate_waiter_id
from datetime import datetime
from src.utils.validators import cpf_validator, name_validator, email_validator, phone_number_validator

class Waiter:
    def __init__(self, name: str, cpf: str, wage: float, email: str, phone_number: str):
        self.waiter_id = generate_waiter_id()       
        self._name = name_validator(name=name)                 
        self._cpf = cpf_validator(cpf=cpf) 
        self._wage = wage                
        self._email = email_validator(email=email)                 
        self._phone_number = phone_number_validator(phone_number=phone_number)                
        self._hire_date = datetime.now().date()          
