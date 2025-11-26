from .models import Task
from .schemas import TaskCreate
from sqlalchemy.orm import Session

def create_task(db : Session, task: TaskCreate):
    task = Task(**task.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
