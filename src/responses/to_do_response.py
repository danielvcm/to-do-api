from pydantic import BaseModel
from .status_response import StatusResponse
from .tag_response import TagResponse
from typing import List, Optional
from datetime import datetime

class ToDoResponse(BaseModel):
    id: int
    name: str
    status: StatusResponse
    description: Optional[str] = None
    tags: Optional[List[TagResponse]] = []
    due_date:  Optional [datetime] = None
