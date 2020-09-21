from pydantic import BaseModel
class TagRequest(BaseModel):
    id: int
    id_user: int
    name: str
