from pydantic import BaseModel

class UpdateNameToDoRequest(BaseModel):
    id: int
    id_user: int
    name: str