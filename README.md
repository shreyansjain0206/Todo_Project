# To-do Project

## Overview
This project is a To-Do List Web Application built using Python and Django. It provides RESTful APIs for managing tasks and a web interface using Django templates.

The application allows users to:
- Create tasks
- Retrieve tasks
- Update tasks
- Delete tasks

Tasks are stored in a SQLite database using raw SQL queries (no ORM).

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone <repository-url>
cd todo_project
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations (if required)
```bash
python manage.py migrate
```

### 5️⃣ Run Server
```bash
python manage.py runserver
```

Application will run at: `http://127.0.0.1:8000`

---

## 🗄 Database Schema

### Table: `tasks`

| Field       | Type    | Description                    |
|-------------|---------|--------------------------------|
| id          | Integer | Primary Key                    |
| title       | Text    | Task title                     |
| description | Text    | Task description               |
| due_date    | Date    | Due date                       |
| status      | Text    | Task status (pending/completed)|

---

## 🚀 API Endpoints

### 1️⃣ Create Task

**Endpoint**
```
POST /api/tasks/create/
```

**Request Body (JSON)**
```json
{
  "title": "Complete Assignment",
  "description": "Finish Django assignment",
  "due_date": "2026-03-12",
  "status": "pending"
}
```

**Response**
```json
{
  "message": "Task created successfully"
}
```

---

### 2️⃣ Get All Tasks

**Endpoint**
```
GET /api/tasks/
```

**Response**
```json
[
  {
    "id": 1,
    "title": "Complete Assignment",
    "description": "Finish Django assignment",
    "due_date": "2026-03-12",
    "status": "pending"
  }
]
```

---

### 3️⃣ Update Task

**Endpoint**
```
POST /api/tasks/update/<task_id>/
```

**Example**
```
POST /api/tasks/update/1/
```

**Request Body**
```
title=Updated Task
description=Updated description
due_date=2026-03-15
status=completed
```

**Response**
```json
{
  "message": "Task updated successfully"
}
```

---

### 4️⃣ Delete Task

**Endpoint**
```
POST /api/tasks/delete/<task_id>/
```

**Example**
```
POST /api/tasks/delete/1/
```

**Response**
```json
{
  "message": "Task deleted successfully"
}
```

---

## 🖥 Web Interface
Task List

<img width="481" height="279" alt="image" src="https://github.com/user-attachments/assets/23a596ad-6436-4001-8b00-03b53e4d59b3" />

Add task

<img width="327" height="264" alt="image" src="https://github.com/user-attachments/assets/614f2e48-9615-41d3-af26-be6877ba4279" />

update task

<img width="314" height="411" alt="image" src="https://github.com/user-attachments/assets/46209a20-2a41-4eb2-b920-14867ea939a0" />

Delete Task

<img width="307" height="228" alt="image" src="https://github.com/user-attachments/assets/233ba236-3fb1-4d03-9153-bb3d4c40cc7e" />




The application also provides a simple web interface using Django Templates.

| Page        | URL                    |
|-------------|------------------------|
| Task List   | `/tasks`               |
| Add Task    | `/tasks/add`           |
| Update Task | `/tasks/update/<id>`   |
| Delete Task | `/tasks/delete/<id>`   |

Users can manage tasks through the UI, which internally calls the API endpoints.

---

## 🧪 Testing

Testing is implemented using pytest. To run tests:
```bash
pytest
```

Tests cover:
- Create task API
- Retrieve tasks API
- Update task API
- Delete task API

<img width="1597" height="153" alt="image" src="https://github.com/user-attachments/assets/9e5d112f-e913-4d09-940f-51cb0a597aff" />

---

## 📊 Logging

Logging is implemented using Python's `logging` module. Logs capture:
- Successful task creation
- Task updates
- Task deletion
- API errors and exceptions

<img width="305" height="88" alt="image" src="https://github.com/user-attachments/assets/e8897150-7962-437f-ac4f-8645cf93a59e" />




<img width="294" height="36" alt="image" src="https://github.com/user-attachments/assets/3b794ae6-fb36-47cf-b5bc-ae62e53d9147" />

---

## ⚠️ Exception Handling

All API endpoints include `try-except` blocks to handle runtime errors and return appropriate error responses.

**Example**
```json
{
  "error": "Failed to create task."
}
```

---

## 🔧 Technologies Used

- Python
- Django
- SQLite
- Pytest
- HTML Templates

---

## 📌 Notes

- Raw SQL queries are used instead of Django ORM as per the assignment requirement.
- Exception handling and logging are implemented for robustness.
- The project follows RESTful API design principles.
