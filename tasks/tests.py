import pytest
import json
from django.test import Client
from django.db import connection

client = Client()

@pytest.fixture(autouse=True)
def create_tasks_table():
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date DATE,
            status TEXT DEFAULT 'pending'
        )
        """)

@pytest.mark.django_db
def test_create_task():

    payload = {
        "title": "Test Task",
        "description": "Testing create",
        "due_date": "2026-03-20",
        "status": "pending"
    }

    response = client.post(
        "/api/tasks/create",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Task created successfully"


@pytest.mark.django_db
def test_get_tasks():

    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO tasks (title, description, due_date, status) VALUES (%s,%s,%s,%s)",
            ["Sample Task", "Sample Desc", "2026-03-20", "pending"]
        )

    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.django_db
def test_update_task():

    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO tasks (title, description, due_date, status) VALUES (%s,%s,%s,%s)",
            ["Old Task", "Old Desc", "2026-03-20", "pending"]
        )

        task_id = cursor.lastrowid

    response = client.post(
        f"/api/tasks/update/{task_id}",
        data={
            "title": "Updated Task",
            "description": "Updated Desc",
            "due_date": "2026-03-25",
            "status": "completed"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Task updated successfully"


@pytest.mark.django_db
def test_delete_task():

    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO tasks (title, description, due_date, status) VALUES (%s,%s,%s,%s)",
            ["Delete Task", "Delete Desc", "2026-03-20", "pending"]
        )

        task_id = cursor.lastrowid

    response = client.post(f"/api/tasks/delete/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"