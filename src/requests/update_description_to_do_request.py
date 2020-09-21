from pydantic import BaseModel

class UpdateDescriptionToDoRequest(BaseModel):
    id: int
    id_user: int
    description: str