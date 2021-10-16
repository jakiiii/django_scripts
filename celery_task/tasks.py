from __future__ import absolute_import, unicode_literals
import sys

from django.core.management import call_command

from celery import shared_task
# from celery import task  # The "task" is no longer in version 5.x You can use version 4.x
from celery.utils.log import get_task_logger

from .email import send_review_email
logger = get_task_logger(__name__)


@shared_task()
def add(x, y):
    return x + y


@shared_task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    logger.info('Sent review email')
    return send_review_email(name, email, review)


@shared_task
def backup():
    sys.stdout = open('celery_task/db.json', 'w')
    call_command('dumpdata', '--indent=2', 'celery_task')
