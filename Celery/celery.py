# coding=utf-8

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


app = Celery('tcelery', backend='amqp://guest@localhost//',
             broker='redis://localhost:6379/0')  # 创建app实例，并指定backend和broker均为rabbitMQ
# app = Celery('tcelery', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
app.conf.CELERY_IGNORE_RESULT = False  # 结果不忽略
# app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' #结果保存在redis中

app.config_from_object('django.conf:settings')  # 从文件中加载实例
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  # 自动加载tasks，注意：他会去app下面查找tasks.py文件，所以我们必须将task放在tasks.py文件中


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
