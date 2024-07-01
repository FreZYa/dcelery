import os
from celery import Celery
from kombu import Queue, Exchange


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True

# app.conf.task_routes = {'newapp.tasks.task1': {'queue': 'queue1'}, 'newapp.tasks.task2': {'queue': 'queue2'},}
# app.conf.task_default_rate_limit = '1/m'
# app.conf.broker_transport_options = {
#     "priority_steps": list(range(10)),
#     "sep": ":",
#     "queue_order_strategy": "priority",
# }
app.autodiscover_tasks()