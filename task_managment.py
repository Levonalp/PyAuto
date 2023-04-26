import pandas as pd
import schedule
import time
from datetime import datetime

tasks = pd.DataFrame(columns=['task_id', 'task_name', 'due_date', 'status'])
appointments = pd.DataFrame(
    columns=['appointment_id', 'property_id', 'date_time', 'status'])


def add_task(task_id, task_name, due_date):
    global tasks
    new_task = pd.DataFrame({'task_id': [task_id], 'task_name': [task_name],
                             'due_date': [due_date], 'status': ['pending']})
    tasks = pd.concat([tasks, new_task], ignore_index=True)


def add_appointment(appointment_id, property_id, date_time):
    global appointments
    new_appointment = pd.DataFrame({'appointment_id': [appointment_id], 'property_id': [property_id],
                                    'date_time': [date_time], 'status': ['upcoming']})
    appointments = pd.concat(
        [appointments, new_appointment], ignore_index=True)

# Rest of the code remains the same


def update_task_status(task_id, status):
    global tasks
    tasks.loc[tasks['task_id'] == task_id, 'status'] = status


def update_appointment_status(appointment_id, status):
    global appointments
    appointments.loc[appointments['appointment_id']
                     == appointment_id, 'status'] = status


def show_pending_tasks():
    pending_tasks = tasks[tasks['status'] == 'pending']
    print("Pending Tasks:")
    print(pending_tasks)


def show_upcoming_appointments():
    upcoming_appointments = appointments[appointments['status'] == 'upcoming']
    print("Upcoming Appointments:")
    print(upcoming_appointments)


def check_pending_tasks():
    now = datetime.now()
    for index, task in tasks.iterrows():
        if task['status'] == 'pending' and datetime.strptime(task['due_date'], '%Y-%m-%d') <= now:
            update_task_status(task['task_id'], 'overdue')


def check_upcoming_appointments():
    now = datetime.now()
    for index, appointment in appointments.iterrows():
        if appointment['status'] == 'upcoming' and datetime.strptime(appointment['date_time'], '%Y-%m-%d %H:%M') <= now:
            update_appointment_status(appointment['appointment_id'], 'past')


if __name__ == "__main__":
    # Add sample tasks and appointments
    add_task(1, "Appraisal Report for Property 123", "2023-04-20")
    add_task(2, "Market Analysis for Neighborhood XYZ", "2023-04-25")

    add_appointment(1, 123, "2023-04-21 10:00")
    add_appointment(2, 456, "2023-04-22 14:00")

    # Schedule the check_pending_tasks and check_upcoming_appointments functions to run every minute
    schedule.every(1).minutes.do(check_pending_tasks)
    schedule.every(1).minutes.do(check_upcoming_appointments)

    # Show pending tasks and upcoming appointments
    show_pending_tasks()
    show_upcoming_appointments()

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check for scheduled tasks every minute
