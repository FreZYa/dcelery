from celery import chain
from dcelery.celery_config import app


"""
from dcelery.celery_tasks.ex5_error_handling_chain import run_tasks
run_tasks()
"""

@app.task(queue='tasks')
def add(x, y):
    return x + y

@app.task(queue='tasks')
def multiply(z):
    # Simulate an erro rfor demonstration purposes
    if z==0:
        raise ValueError("Error: Division by zero.")
    return z

def run_task_chain():
    task_chain = chain(add.s(2, 3), multiply.s(0))
    result = task_chain.apply_async()
    result.get()