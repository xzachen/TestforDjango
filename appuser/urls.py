#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SundayCoder-俊勇
# @File    : urls.py
from django.urls import path
from appuser import views

# path('articles/<int:year>/', views.year_archive),
urlpatterns = [
    # 路由处理
    path('', views.index, name='index'),
    # 登录的路由 POST
    path('login', views.login, name='login'),
    # 注册的路由 POST
    path('register', views.register, name='register'),
    path('retrievepassword', views.RetrievePassword, name='retrievepassword'),
    # 判断是否登录注册过
    path('registerornot/<str:QQnumber>', views.registerOrNot, name='registerornot'),
    # 查询课程信息路由。方法GET
    path('querycourseinfo/<int:uid>', views.querycourseinfo, name='querycourseinfo'),
    # 更新课程的路由。方法POST
    path('updatecourseinfo', views.updatecourseInfo, name='updatecourseinfo'),
    # 创建课程的路由,方法POST
    path('createcourse', views.createCourse, name='createcourse'),
    # 删除课程信息，方法GET
    path('deletecourse/<int:cid>', views.deleteCourse, name='deletecourse'),
    # 测试文件删除路径，方法POST
    path('uploadfile', views.uploadfile, name='uploadfile'),
    # 测试下载文件的路径
    path('download', views.download, name='download'),
]
