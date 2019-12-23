# coding=utf-8
import datetime
import json
import time
import redis
from django.shortcuts import render

from first.models import Add
from .tasks import test


# Create your views here.


def index(request):
    return render(request, 'first/first_index.html')


def add_1(request):
    try:
        first = int(request.GET.get('first'))
    except:
        first = 0
    try:
        second = int(request.GET.get('second'))
    except:
        second = 0
    result = test.apply_async(args=(first, second))
    dd = Add(task_id=result.id, first=first, second=second, log_date=datetime.datetime.now())
    dd.save()
    return render(request, 'first/first_index.html')


# 任务结果
def results(request):
    # 查询所有的任务信息
    start_time = time.time()
    new_result = {}
    rt_list = []
    rows = Add.objects.all()
    for r in rows:
        status, result = get_status_id(r.task_id)
        new_result["task_id"] = r.task_id
        new_result["first"] = r.first
        new_result["second"] = r.second
        new_result["log_date"] = r.log_date
        new_result["status"] = status
        new_result["result"] = result
        rt_list.append(new_result)
        new_result = {}
    end_time = time.time()
    rt = end_time - start_time
    print(rt,len(rows))
    return render(request, template_name='first/first_result.html', context={'rows': rt_list})


def get_status_id(task_id):
    """
    :param task_id:
    :return:
    坑：host填写主机名时，会耗时非常多，可以通过time获取，大概一次要1s
    task测试：这里
    """
    pool = redis.ConnectionPool(host='127.0.0.1', port=6382, db=1,password=123456)
    r = redis.Redis(connection_pool=pool)
    task_id = 'celery-task-meta-' + task_id
    # start_time = time.time()
    try:
        data = r.get(task_id)
        data = str(data,encoding='utf-8')
        status = json.loads(data).get("status")
        result = json.loads(data).get("result")
    except Exception as e:
        print(e.__class__,e.args)
        status = 'Executing...'
        result = 0
    # end_time = time.time()
    # print 'time:%s' %(end_time-start_time)
    print(status, result)

    return status, result
