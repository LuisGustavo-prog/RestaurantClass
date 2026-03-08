from fastapi import APIRouter
from src.controllers.menu_controller import (
    controller_get_menu,
    controller_get_menu_by_category,
    controller_get_menu_by_name
)

menu = APIRouter()

@menu.get('/menu/')
def get_menu():
    return controller_get_menu()

@menu.get('/menu/category/')
def get_menu_by_category(category: str):
    return controller_get_menu_by_category(category=category)

@menu.get('/menu/name/')
def get_menu_by_name(name: str):
    return controller_get_menu_by_name(name=name)
