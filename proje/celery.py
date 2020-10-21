from __future__ import absolute_import
import os
from celery import Celery



# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proje.settings')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app = Celery('proje')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.schedule_beat={
    'every-15-seconds': {
        'task':'proje.tasks.send_email',
        'schedule':15,
        'args':{'slmkrdmnoglu@gmail.com',}
    }
}
app.autodiscover_tasks()


@app.task(bind=True)
def hello(self):
    print("Hi")

@app.task
def check():
    print("I am doing your stuff")

app.conf.beat_schedule ={
    "run-me-every_ten-seconds": {
        "task":"task.check",
        "schedule": 10.0
    }
}