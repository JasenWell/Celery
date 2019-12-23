# coding=utf-8
from django.conf.urls import url, include
from first import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^result',views.results,name='result'),
    url(r'^add',views.add_1,name='add'),

]
