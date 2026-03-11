CREATE_TASK = """
INSERT INTO tasks (title, description, due_date, status)
VALUES (%s, %s, %s, %s)
"""

GET_TASKS = """
SELECT * FROM tasks
"""

UPDATE_TASK = """
UPDATE tasks
SET title=%s, description=%s, due_date=%s, status=%s
WHERE id=%s
"""

DELETE_TASK = """
DELETE FROM tasks WHERE id=%s
"""