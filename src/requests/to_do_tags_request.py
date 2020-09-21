from pydantic import BaseModel
from typing import List

class ToDoTagsRequest(BaseModel):
    id: int
    id_user: int
    tags: List[str]
