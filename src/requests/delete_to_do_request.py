from pydantic import BaseModel

class DeleteToDoRequest(BaseModel):
    id: int
    id_user: int
    name: str