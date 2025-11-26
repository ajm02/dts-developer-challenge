from sqlalchemy import Column, Integer, String, DateTime, Text
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False)
    due_datetime = Column(DateTime, nullable=False)
