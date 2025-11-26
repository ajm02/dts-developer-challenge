from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, SessionLocal, engine
from .schemas import TaskCreate, TaskResponse
from .crud import create_task
from sqlalchemy.orm import Session

app = FastAPI(title="HMCTS Task API", version="1.0")

Base.metadata.create_all(bind=engine)

origins = ["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def post_task(payload: TaskCreate, db: Session = Depends(get_db)):
    created_task = create_task(db, payload)
    return created_task
