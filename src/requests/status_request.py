from pydantic import BaseModel
class StatusRequest(BaseModel):
    id: int
    id_user: int
    name: str
