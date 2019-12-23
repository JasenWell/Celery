# coding=utf-8

from Celery import celery_app
import time


@celery_app.task
def test(x, y):
    time.sleep(15)
    return x + y
