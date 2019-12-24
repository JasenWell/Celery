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
	
	celery 启动 TypeError: 'NoneType' object is not iterable
	原因 执行此命令pip install django-celery-result 把celery什么的也给更新了，会提示不兼容：
	解决：celery降级到3.X就行了 执行 pip install celery==3.1.26.post2  
	celery 4.0变化比较大，砍了很多不常用的功能，而且不再支持windows，建议大家暂缓使用 新的celery 4.0与 djcelery 3.1.17不兼容


 
 爬虫各阶段
 https://blog.csdn.net/weixin_30920513/article/details/98145396

 https://www.cnblogs.com/skyflask/p/9865378.html
 https://www.cnblogs.com/wdliu/p/9530219.html
 https://blog.csdn.net/bbwangj/article/details/90573640
 https://blog.csdn.net/bbwangj/article/details/90573662
 https://www.jianshu.com/p/ec128512af8e celery 常用配置\
 
 结果存储使用django的orm存储，安装插件  windows下面兼容性不能用
 pip install django-celery-results
 django_celery_results 添加到installed-apps中
 python manage.py migrate django_celery_results
 
 django  使用celery定时任务  windows下面兼容性不能用
 pip install django-celery-beat
 django_celery_beat 添加到installed-apps中
 python manage.py migrate django_celery_beat
 

