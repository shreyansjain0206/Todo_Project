from django.shortcuts import render


import json
import logging
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from . import queries
from django.shortcuts import render, redirect


logger = logging.getLogger(__name__)
# Fetches a single task by ID and loads the delete confirmation page.
# Think of this as the "are you sure?" screen before wiping a task for good.
def delete_task_page(request, task_id):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks WHERE id=%s", [task_id])
        row = cursor.fetchone()
#fetchone() → retrieves one row from the query result.

#The result is returned as a tuple.
    task = {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "due_date": row[3],
        "status": row[4]
    }# it converts a tuple to a dict as it is easy to load into Html template

    return render(request, "tasks/delete_task.html", {"task": task}) 
    #render() → Django function that loads an HTML template.
   # {"task": task} → context data sent to the template.


# Grabs an existing task's data and pre-fills the update form with it.
# Saves the user from retyping everything just to change one field.    
def update_task_page(request, task_id):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks WHERE id=%s", [task_id])
        row = cursor.fetchone()

    task = {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "due_date": row[3],
        "status": row[4]
    }

    return render(request, "tasks/update_task.html", {"task": task})

# Pulls every task from the database and renders them in a list view.
# This is the main page where users see everything on their plate.
def task_page(request):

    with connection.cursor() as cursor:
        cursor.execute(queries.GET_TASKS)
        rows = cursor.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "due_date": row[3],
            "status": row[4]
        })

    return render(request, "tasks/task_list.html", {"tasks": tasks})


# Handles both showing the "add task" form and processing its submission.
# On POST, it saves the new task and bounces the user back to the task list.
def add_task_page(request):

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        with connection.cursor() as cursor:
            cursor. execute(
                queries.CREATE_TASK,
                [title, description, due_date, "pending"]
            )

        return redirect("/tasks")

    return render(request, "tasks/add_task.html")
# API endpoint that accepts a JSON payload and creates a brand-new task.
# Returns a success message or a 500 if something goes sideways.
@csrf_exempt
#skip Django's security token check — used on API endpoints because external apps don't have that token 🎯
def create_task(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            title = data.get("title")
            description = data.get("description")
            due_date = data.get("due_date")
            status = data.get("status")

            with connection.cursor() as cursor:
                cursor. execute(
                    queries.CREATE_TASK,
                    [title, description, due_date, status]
                )

            logger.info("Task created successfully")

            return JsonResponse({"message": "Task created successfully"})

        except Exception as e:
            logger.error(f"Error creating task: {str(e)}")

            return JsonResponse({
                "error": "Failed to create task."
            }, status=500)

    return JsonResponse({"error": "POST request required"}, status=400)
# Fetches all tasks from the database and returns them as a JSON list.
# Handy for any frontend or external service that needs the full task feed.
def get_tasks(request):

    try:
        with connection.cursor() as cursor:
            cursor.execute(queries.GET_TASKS)
            rows = cursor.fetchall()

        tasks = []

        for row in rows:
            tasks.append({
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "due_date": row[3],
                "status": row[4]
            })

        return JsonResponse(tasks, safe=False)

    except Exception as e:
        logger.error(f"Error fetching tasks: {str(e)}")

        return JsonResponse({
            "error": "Failed to retrieve tasks."
        }, status=500)
# Takes updated field values from a POST form and applies them to an existing task.
# Logs the change and lets the caller know if the update succeeded or failed.
@csrf_exempt
def update_task(request, task_id):

    if request.method == "POST":

        try:
            title = request.POST.get("title")
            description = request.POST.get("description")
            due_date = request.POST.get("due_date")
            status = request.POST.get("status")

            with connection.cursor() as cursor:
                cursor. execute(
                    queries.UPDATE_TASK,
                    [title, description, due_date, status, task_id]
                )

            logger.info(f"Task {task_id} updated successfully")

            return JsonResponse({"message": "Task updated successfully"})

        except Exception as e:
            logger.error(f"Error updating task {task_id}: {str(e)}")

            return JsonResponse({
                "error": "Failed to update task."
            }, status=500)

    return JsonResponse({"error": "POST request required"}, status=400)

# Permanently removes a task from the database using its ID.
# Once it's gone, it's gone — logs the action either way
@csrf_exempt
def delete_task(request, task_id):

    if request.method == "POST":

        try:
            with connection.cursor() as cursor:
                cursor.execute(queries.DELETE_TASK, [task_id])

            logger.info(f"Task {task_id} deleted successfully")

            return JsonResponse({"message": "Task deleted successfully"})

        except Exception as e:
            logger.error(f"Error deleting task {task_id}: {str(e)}")

            return JsonResponse({
                "error": "Failed to delete task."
            }, status=500)


    return JsonResponse({"error": "POST request required"}, status=400)



#One set of functions renders HTML templates for browser-based interaction, while the other set exposes REST-style API endpoints that return JSON responses. The HTML views are used for server-side rendered pages, while the APIs allow external clients such as mobile apps or frontend frameworks to interact with the same backend.
