from src.entities.id_generetor import IDGenerato
from datetime import datetime
from src.utils.validators import cpf_validator, name_validator

class Waiter:
    def __init__(self, name, cpf, email, phone_number):
        self._id = IDGenerato.generate_waiter()                 
        self._name = name_validator(name=name)                 
        self._cpf = cpf_validator(cpf=cpf)                 
        self._email = email                 
        self._phone_number = phone_number                
        self._hire_date = datetime.now().date()          

    def __str__(self) -> str:
        return f'Name: {self._name}\nID: {self._id}\nCPF: {self._cpf}\nEmail: {self._email}\nPhone Number: {self._phone_number}\nHire Date: {self._hire_date}'
    