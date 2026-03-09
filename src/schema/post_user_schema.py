from pydantic import BaseModel

class PostUserSchema(BaseModel):
    table_number: int
    waiter_id: int
    main_course: str = ''
    drink: str = ''
    starter: str = ''
