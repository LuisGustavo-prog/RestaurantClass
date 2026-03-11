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

    @classmethod   
    def get_all_waiters(cls):
        waiter = list(waiter_collection.find({}, {'_id': 0}))

        if not waiter:
            return {'error': True, 'message': 'Waiter not found.'}

        return waiter

    @classmethod
    def get_waiters_by_id(cls, waiter_id: int):
        waiter = waiter_collection.find_one({'waiter_id': waiter_id}, {'_id': 0})

        if waiter is None:
            return {'error': True, 'message': f'Waiter {waiter_id} not found.'}
        
        return waiter
    
    @classmethod
    def update_waiter(cls, waiter_id: int, new_name: str = None, new_wage: float = None, new_email: str = None, new_phone_number: str = None):
        waiter = waiter_collection.find_one({'waiter_id': waiter_id}, {'_id': 0})

        if waiter is None:
            return {'error': True, 'message': f'Waiter {waiter_id} not found.'}

        updated_fields = {}

        if new_name and new_name.strip():
            updated_fields['name'] = name_validator(name=new_name)

        if new_wage:
            updated_fields['wage'] = new_wage

        if new_email and new_email.strip():
            updated_fields['email'] = email_validator(email=new_email)

        if new_phone_number and new_phone_number.strip():
            updated_fields['phone_number'] = phone_number_validator(phone_number=new_phone_number)
                
        waiter_collection.update_one(
            {'waiter_id': waiter_id},
            {'$set': updated_fields}
        )

        return {'error': False, 'message': 'Waiter updated successfully.'}
    

    @classmethod
    def delete_waiter(cls, waiter_id: int):
        waiter = waiter_collection.find_one({'waiter_id': waiter_id})

        if waiter is None:
            return {'error': True, 'message': f'Waiter {waiter_id} not found.'}
        
        waiter_collection.delete_one({'waiter_id': waiter_id})

        return {'error': False, 'message': 'Waiter successfully deleted.'}
    