from pydantic import BaseModel

class UpdateStatusToDoRequest(BaseModel):
    id: int
    id_user: int
    status: str