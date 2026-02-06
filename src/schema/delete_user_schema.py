from pydantic import BaseModel

class DeleteUserSchema(BaseModel):
    table_number: int = None
    item_number: int = None
    type_of_choice: str = 'all'
