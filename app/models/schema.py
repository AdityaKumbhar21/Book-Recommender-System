
from pydantic import BaseModel

class UserRequest(BaseModel):
    book_name: str