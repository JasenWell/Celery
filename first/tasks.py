# coding=utf-8

from Celery import celery_app


@celery_app.task
def test(x, y):
    return x + y
