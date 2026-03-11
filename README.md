# Todo_Project
Overview

This project is a To-Do List Web Application built using Python and Django. It provides RESTful APIs for managing tasks and a web interface using Django templates.

The application allows users to:

Create tasks

Retrieve tasks

Update tasks

Delete tasks

Tasks are stored in a SQLite database using raw SQL queries (no ORM).

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <repository-url>
cd todo_project
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations (if required)
python manage.py migrate
5️⃣ Run Server
python manage.py runserver

Application will run at:
http://127.0.0.1:8000

🗄 Database Schema
Table: tasks

Field	Type	Description
id	Integer	Primary Key
title	Text	Task title
description	Text	Task description
due_date	Date	Due date
status	Text	Task status (pending/completed)

🚀 API Endpoints
1️⃣ Create Task

Endpoint

POST /api/tasks/create/

Request Body (JSON)
 {
"title": "Complete Assignment",
"description": "Finish Django assignment",
"due_date": "2026-03-12",
"status": "pending"
}
Response
{
"message": "Task created successfully"
}

2️⃣ Get All Tasks
Endpoint
GET /api/tasks/
Response
[
{
"id": 1,
"title": "Complete Assignment",
"description": "Finish Django assignment",
"due_date": "2026-03-12",
"status": "pending"
}
]

3️⃣ Update Task
Endpoint
POST /api/tasks/update/<task_id>/
Example
POST /api/tasks/update/1/
Request Body
title=Updated Task
description=Updated description
due_date=2026-03-15
status=completed
Response
{
"message": "Task updated successfully"
}

4️⃣ Delete Task
Endpoint
POST /api/tasks/delete/<task_id>/
Example
POST /api/tasks/delete/1/
Response
{
"message": "Task deleted successfully"
}



🖥 Web Interface

The application also provides a simple web interface using Django Templates.

Available pages:
Page	URL
Task List	/tasks
Add Task	/tasks/add
Update Task	/tasks/update/<id>
Delete Task	/tasks/delete/<id>
Users can manage tasks through the UI, which internally calls the API endpoints.

🧪 Testing
Testing is implemented using pytest.
To run tests:
pytest
Tests cover:
Create task API
Retrieve tasks API
Update task API
Delete task API
All API endpoints are tested for correct functionality.

📊 Logging
Logging is implemented using Python's logging module.
Logs capture:
Successful task creation
Task updates
Task deletion
API errors and exceptions

⚠ Exception Handling
All API endpoints include try-except blocks to handle runtime errors and return appropriate error responses.
Example:
{
"error": "Failed to create task."
}
🔧 Technologies Used
Python
Django
SQLite
Pytest
HTML Templates

📌 Notes
Raw SQL queries are used instead of Django ORM as per the assignment requirement.
Exception handling and logging are implemented for robustness.
The project follows RESTful API design principles.

