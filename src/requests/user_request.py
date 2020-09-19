from pydantic import BaseModel
class UserRequest(BaseModel):
    name: str
    user_name: str
    password: str