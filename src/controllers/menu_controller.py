from src.entities.menu import Menu

def controller_get_menu():
    return Menu.get_menu()

def controller_get_menu_by_category(category: str):
    return Menu.get_by_category(category=category)

def controller_get_menu_by_name(name: str):
    return Menu.get_by_name(name=name)