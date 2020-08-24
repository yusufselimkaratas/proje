# Create your tasks here

from proje.celery import app



@app.task(bind=True)
def hello(self):
    print("Hello There!")