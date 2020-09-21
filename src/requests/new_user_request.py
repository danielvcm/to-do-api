from pydantic import BaseModel
class NewUserRequest(BaseModel):
    name: str
    user_name: str
    password: str