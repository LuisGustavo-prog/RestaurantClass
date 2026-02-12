from validate_docbr import CPF
import re

def cpf_validator(cpf: str) -> str:
    validador = CPF()
    
    if validador.validate(cpf):
        return cpf

    raise ValueError('Error: CPF inválido!')

def name_validator(name: str) -> str:
    name_join = ' '.join(name.strip().split())

    if not name_join:
        raise ValueError('Error: Nome não pode estar vazio.')
    
    if len(name_join) < 3:
        raise ValueError('Error: Nome muito curto.')
    
    if len(name_join) > 100:
        raise ValueError('Error: Nome muito extenso.')
    
    default = r'^[A-Za-zÀ-ÿ\s\'-]+$'
    if not re.match(default, name_join):
        raise ValueError('Error: Nome contém caracteres inválidos')
    
    if not any(x.isalpha() for x in name_join):
        raise ValueError('Error: Nome deve conter letras')

    return name
