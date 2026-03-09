from pydantic import BaseModel
from typing import Optional

class PutUserSchema(BaseModel):
    table_number: int
    item_id: int
    new_main_course: Optional[str] = None
    new_drink: Optional[str] = None
    new_starter: Optional[str] = None
    