from pydantic import BaseModel
from typing import List

class RemoveToDoTagRequest(BaseModel):
    id_to_do: int
    id_tag: int
