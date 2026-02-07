import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.entities.waiter import Waiter
from src.utils.validators import cpf_validator

waiter1 = Waiter(
    name='João Silva',
    cpf='111.444.777-35',
    email='joao.silva@restaurante.com',
    phone_number='(11) 98765-4321'
)

waiter2 = Waiter(
    name='Maria Santos',
    cpf='987.654.321-00',
    email='maria.santos@restaurante.com',
    phone_number='(11) 91234-5678'
)

waiter3 = Waiter(
    name='Carlos Oliveira',
    cpf='390.533.447-05',
    email='carlos.oliveira@restaurante.com',
    phone_number='(11) 99876-5432'
)

print(waiter1, '\n')
print(waiter2, '\n')
print(waiter3)


# Lista com alguns cpfs válidos.
cpfs_validos = [
    '529.982.247-25',
    '111.444.777-35',
    '390.533.447-05',
    '862.368.077-09',
    '213.059.327-09',
    '855.444.047-30',
    '739.624.697-02',
    '426.653.058-94',
    '145.371.206-72',
    '301.242.501-44',
    '750.185.367-10',
    '923.097.134-16',
    '468.319.654-72',
    '637.828.194-72',
    '891.625.734-63',
    '074.563.981-20',
    '258.147.369-85',
    '369.258.147-96',
    '147.258.369-74',
    '963.852.741-85'
]