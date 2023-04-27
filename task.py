import datetime
import pytz
import schedule
import time


class Task:
    def __init__(self, task_id, description, due_date, appointment_date=None, is_complete=False):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.appointment_date = appointment_date
        self.is_complete = is_complete

    def complete_task(self):
        self.is_complete = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.complete_task()
                break

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.is_complete]

    def get_overdue_tasks(self):
        now = datetime.datetime.now(pytz.utc)
        return [task for task in self.tasks if not task.is_complete and task.due_date < now]

    def schedule_appointment(self, task_id, appointment_date):
        for task in self.tasks:
            if task.task_id == task_id:
                task.appointment_date = appointment_date
                break

def add_task(task_manager, description, due_date, appointment_date=None):
    task_id = len(task_manager.tasks) + 1
    task = Task(task_id, description, due_date, appointment_date)
    task_manager.add_task(task)

def complete_task(task_manager, task_id):
    task_manager.complete_task(task_id)

def schedule_appointment(task_manager, task_id, appointment_date):
    task_manager.schedule_appointment(task_id, appointment_date)

def display_tasks(task_manager):
    pending_tasks = task_manager.get_pending_tasks()
    overdue_tasks = task_manager.get_overdue_tasks()

    print("Pending tasks:")
    for task in pending_tasks:
        print(f"Task ID: {task.task_id}, Description: {task.description}, Due Date: {task.due_date}")

    print("\nOverdue tasks:")
    for task in overdue_tasks:
        print(f"Task ID: {task.task_id}, Description: {task.description}, Due Date: {task.due_date}")


# Create a TaskManager instance
task_manager = TaskManager()

# Add tasks
due_date = datetime.datetime.now(pytz.utc) + datetime.timedelta(days=3)
add_task(task_manager, "Task 1", due_date)

due_date = datetime.datetime.now(pytz.utc) + datetime.timedelta(days=1)
add_task(task_manager, "Task 2", due_date)

# Schedule an appointment
appointment_date = datetime.datetime.now(pytz.utc) + datetime.timedelta(days=2)
schedule_appointment(task_manager, 2, appointment_date)

