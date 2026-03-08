from pydantic import BaseModel

class PutUserSchema(BaseModel):
    table_number: int
    item_id: int
    new_main_course: str = ''
    new_drink: str = ''
    new_starter: str = ''
