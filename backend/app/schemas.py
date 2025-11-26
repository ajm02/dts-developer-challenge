from pydantic import BaseModel, Field, validator
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    status: StatusEnum
    due_datetime: datetime

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
