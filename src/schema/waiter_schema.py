from pydantic import BaseModel, field_validator
from typing import Optional

class CreateWaiterSchema(BaseModel):
    name: str
    cpf: str
    wage: float
    email: str
    phone_number: str

class UpdateWaiterSchema(BaseModel):
    waiter_id: int
    new_name: Optional[str] = None
    new_wage: Optional[float] = None
    new_email: Optional[str] = None
    new_phone_number: Optional[str] = None


    @field_validator('new_name', 'new_email', 'new_phone_number', mode='before')
    def mpty_to_none(cls, value):
        if value == '' or value == 'string':
            return None
        return value

class DeleteWaiterSchema(BaseModel):
    waiter_id: int