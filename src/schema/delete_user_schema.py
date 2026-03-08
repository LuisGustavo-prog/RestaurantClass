from pydantic import BaseModel

class DeleteOrderSchema(BaseModel):
    table_number: int

class DeleteItemSchema(BaseModel):
    table_number: int
    item_id: int
