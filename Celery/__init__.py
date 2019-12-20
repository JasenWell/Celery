# coding=utf-8
# 绝对导入，以免celery和标准库中的celery模块冲突
from __future__ import absolute_import
# 以下导入时为了确保在Django启动时加载app，shared_task在app中会使用到
from .celery import app as celery_app
