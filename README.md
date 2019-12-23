# Celery
 异步框架，定时任务处理框架

 介绍链接
 https://www.jianshu.com/p/620052aadbff 
 https://blog.csdn.net/cuomer/article/details/81214438

 
 https://files.pythonhosted.org/packages/ 虚拟路径新增仓库url  
 https://blog.csdn.net/Dontla/article/details/100176224  将项目包导出到requirements.txt中,批量安装
 
 
 django框架下的celery,可以进入项目虚拟环境安装
 pip install celery
 pip install django-celery
 pip install flower
 
 celery 启动
 python manage.py celery worker -c 6 -l INFO   //开启6个子进程进行处理 日志级别为info
 使用redis和celery执行异步任务时报错AttributeError: 'str' object has no attribute 'items'  
  问题原因：

	redis版本问题，版本高了。

	解决办法：
	报错版本redis=3.2.1，降低版本到redis=2.10.6，虚拟环境下使用命令pip install redis==2.10.6

 
 爬虫各阶段
 https://blog.csdn.net/weixin_30920513/article/details/98145396

 https://www.cnblogs.com/skyflask/p/9865378.html
 https://www.cnblogs.com/wdliu/p/9530219.html
 https://blog.csdn.net/bbwangj/article/details/90573640
 

