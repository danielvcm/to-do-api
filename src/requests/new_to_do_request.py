from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class NewToDoRequest(BaseModel):
    id_user: int
    name: str
    status: str
    description: Optional [str] = None
    tags: Optional [List[str]] = []
    due_date: Optional [datetime] = None