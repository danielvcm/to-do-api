from pydantic import BaseModel
from datetime import datetime

class UpdateDueDateToDoRequest(BaseModel):
    id: int
    id_user: int
    due_date: datetime