from pydantic import BaseModel

class PostUserSchema(BaseModel):
    table_number: int
    main_course: str = ''
    drink: str = ''
    salad: str = ''
