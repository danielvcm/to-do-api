from pydantic import BaseModel
class NewStatusRequest(BaseModel):
    id_user: int
    name: str
