from pydantic import BaseModel
class StatusResponse(BaseModel):
    id: int
    name: str
