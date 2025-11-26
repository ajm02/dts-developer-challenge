from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app=app)
TASKS_PATH = "/tasks"


def test_create_task_success():
    payload = {
        "title": "Test task",
        "description": "A test description",
        "status": "todo",
        "due_datetime": "2030-01-01T12:00:00",
    }

    response = client.post(TASKS_PATH, json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == "Test task"


def test_create_task_failure():
    payload = {
        "title": "",
        "description": "A test description",
        "status": "todo",
        "due_datetime": "invalid",
    }

    response = client.post(TASKS_PATH, json=payload)
    assert response.status_code in (400, 422)
