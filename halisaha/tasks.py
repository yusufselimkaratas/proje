# Create your tasks here
from django_celery_beat.schedulers import DatabaseScheduler

from proje.celery import app
from celery import shared_task


from time import sleep

@shared_task
def send_email(email):
    print('Sample message is sent to {email}')
