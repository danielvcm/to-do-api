from pydantic import BaseModel
class NewTagRequest(BaseModel):
    id_user: int
    name: str
