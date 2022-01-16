# -*- encoding: utf-8 -*-
"""
@File    : account.py
@Time    : 2021-12-15 22:04
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from django.shortcuts import HttpResponse, render, redirect
from rbac import models
from rbac.service.init_Permission import init_Permission


def login(request):
    # 1. 用户登录
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})
    init_Permission(current_user,request)

    return redirect('/customer/list/')