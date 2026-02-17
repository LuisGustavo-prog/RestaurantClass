import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.entities.order import Order
from src.entities.waiter import Waiter

# Teste no terminal

print("=" * 60)
print("CRIANDO 3 PEDIDOS")
print("=" * 60)

# Pedido 1 - Mesa 1
pedido1 = Order(table_number=1, main_course='Pizza', drink='Coca-Cola', salad='Caesar')
pedido1.post_order(table_number=1, main_course='Hamburguer', drink='Suco')

# # Pedido 2 - Mesa 2
pedido2 = Order(table_number=30, main_course='Lasanha', drink='Água', salad='Verde')
pedido2.post_order(table_number=2, main_course='Frango', drink='Refrigerante')

# Pedido 3 - Mesa 3
pedido3 = Order(table_number=3, main_course='Macarrão', drink='Vinho')

print("\n" + "=" * 60)
print("VISUALIZANDO TODOS OS PEDIDOS")
print("=" * 60)
print(Order.get_order(type_of_choice='all'))

print("\n" + "=" * 60)
print("ATUALIZANDO ITEM 1 DA MESA 1")
print("=" * 60)
resultado = Order.put_order(table=1, item_number=1, new_main_course='Picanha', new_drink='Cerveja')
print(resultado)

print("\n" + "=" * 60)
print("DELETANDO ITEM 2 DA MESA 2")
print("=" * 60)
print(Order.delete_order(table_number=2, item_number=2, type_of_choice='specific'))

print("\n" + "=" * 60)
print("VISUALIZANDO PEDIDOS APÓS DELETAR ITEM")
print("=" * 60)
print(Order.get_order_terminal(type_of_choice='all'))

print("\n" + "=" * 60)
print("DELETANDO MESA 3 COMPLETA")
print("=" * 60)
print(Order.delete_order(table_number=3, type_of_choice='specific'))

print("\n" + "=" * 60)
print("VISUALIZANDO PEDIDOS FINAIS")
print("=" * 60)
print(Order.get_order_terminal(type_of_choice='all'))
