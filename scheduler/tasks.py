import time
from datetime import datetime
# from celery import shared_task
from django_celery.celery import app

# @shared_task
# @app.task(bind=True, name='task_1')
@app.task
def task_1():
    time.sleep(2)
    date_str = datetime.now().__str__()
    print("Time: {} - Run Task 1".format(date_str))


# @shared_task
@app.task
# @app.task(bind=True, name='task_2')
def task_2():
    time.sleep(3)
    date_str = datetime.now().__str__()
    print("Time: {} - Run Task 2".format(date_str))