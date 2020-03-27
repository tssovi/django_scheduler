import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django scheduler configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run-task-1': {
        'task': 'scheduler.tasks.task_1',
        'schedule': 2.0
    },
    'run-task-2': {
        'task': 'scheduler.tasks.task_2',
        'schedule': 3.0
    }
}