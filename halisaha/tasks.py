# Create your tasks here

from celery import shared_task



@shared_task
def hello():
    print("Hello There!")