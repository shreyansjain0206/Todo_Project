from django.shortcuts import render

# Create your views here.
import json
import logging
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from . import queries
from django.shortcuts import render, redirect


logger = logging.getLogger(__name__)

def delete_task_page(request, task_id):

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

    return render(request, "tasks/delete_task.html", {"task": task})

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


def add_task_page(request):

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        with connection.cursor() as cursor:
            cursor.execute(
                queries.CREATE_TASK,
                [title, description, due_date, "pending"]
            )

        return redirect("/tasks")

    return render(request, "tasks/add_task.html")

@csrf_exempt
def create_task(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            title = data.get("title")
            description = data.get("description")
            due_date = data.get("due_date")
            status = data.get("status")

            with connection.cursor() as cursor:
                cursor.execute(
                    queries.CREATE_TASK,
                    [title, description, due_date, status]
                )

            logger.info("Task created successfully")

            return JsonResponse({"message": "Task created successfully"})

        except Exception as e:
            logger.error(f"Error creating task: {str(e)}")

            return JsonResponse({
                "error": "Failed to create task"
            }, status=500)

    return JsonResponse({"error": "POST request required"}, status=400)
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
            "error": "Failed to retrieve tasks"
        }, status=500)
@csrf_exempt
def update_task(request, task_id):

    if request.method == "POST":

        try:
            title = request.POST.get("title")
            description = request.POST.get("description")
            due_date = request.POST.get("due_date")
            status = request.POST.get("status")

            with connection.cursor() as cursor:
                cursor.execute(
                    queries.UPDATE_TASK,
                    [title, description, due_date, status, task_id]
                )

            logger.info(f"Task {task_id} updated successfully")

            return JsonResponse({"message": "Task updated successfully"})

        except Exception as e:
            logger.error(f"Error updating task {task_id}: {str(e)}")

            return JsonResponse({
                "error": "Failed to update task"
            }, status=500)

    return JsonResponse({"error": "POST request required"}, status=400)
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
                "error": "Failed to delete task"
            }, status=500)

    return JsonResponse({"error": "POST request required"}, status=400)