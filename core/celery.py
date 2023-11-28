# print(f'Celery file loading')
# self.stdout.write('\nTesting redis...')

# import os
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
#
# app = Celery('app')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
#
#


import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(name="core.add")
def add(x, y):
    return x + y

# @app.task
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
