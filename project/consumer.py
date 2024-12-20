import os

from celery import Celery

celery_app = Celery(
    __name__,
    broker=os.environ.get('CELERY_BROKER_URL', ''),
    backend=os.environ.get('CELERY_RESULT_BACKEND', '')
)
print(os.environ.get('CELERY_RESULT_BACKEND', ''))

celery_app.config_from_object('celery_config.config', namespace='CELERY')
