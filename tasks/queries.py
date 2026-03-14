#A Python variable named CREATE_TASK is created.
#It stores a multi-line SQL query string using triple quotes
# %S is used to put values in the task table. It helps in the prevention of SQL injection to prevent hackers
CREATE_TASK = """
INSERT INTO tasks (title, description, due_date, status) 
VALUES (%s, %s, %s, %s) 
"""
# Get task is used to get a list of tasks
GET_TASKS = """
SELECT * FROM tasks
"""
#"Go to the tasks table, find the task with a specific ID, and update its title, description, due date, and status. Without making any changes, will update all tasks
UPDATE_TASK = """
UPDATE tasks
SET title=%s, description=%s, due_date=%s, status=%s
WHERE id=%s
"""
# used to delete the task of ID 
DELETE_TASK = """
DELETE FROM tasks WHERE id=%s
"""
