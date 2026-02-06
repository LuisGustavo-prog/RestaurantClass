from pydantic import BaseModel

class PutUserSchema(BaseModel):
    table: int
    item: int
    new_main_course: str = ''
    new_drink: str = ''
    new_salad: str = ''
