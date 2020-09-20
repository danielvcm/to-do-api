from pydantic import BaseModel
class StatusResponse(BaseModel):
    id: int
    id_user: int
    name: str
