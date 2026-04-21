from validate_docbr import CPF
import re

def cpf_validator(cpf: str):
    validador = CPF()
    
    if validador.validate(cpf):
        return cpf

    raise ValueError('Error: Invalid CPF!')

def name_validator(name: str) -> str:
    name_join = ' '.join(name.strip().split())

    if not name_join:
        raise ValueError('Error: Name cannot be empty.')
    
    if len(name_join) < 3:
        raise ValueError('Error: Name is too short.')
    
    if len(name_join) > 100:
        raise ValueError('Error: Name is too long.')
    
    default = r'^[A-Za-zÀ-ÿ\s\'-]+$'
    if not re.match(default, name_join):
        raise ValueError('Error: Name contains invalid characters.')
    
    if not any(x.isalpha() for x in name_join):
        raise ValueError('Error: Name must contain letters.')

    return name

def email_validator(email: str):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        raise ValueError('Error: Invalid email.')
    
    return email

def phone_number_validator(phone_number: str):
    pattern = r'^\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}$'

    if not re.match(pattern, phone_number):
        raise ValueError('Error: Invalid phone number.')
    
    return phone_number
