# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    : 2021-12-26 11:58
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django import forms
from django.forms.widgets import TextInput

from rbac import models
from rbac.forms.role import RoleModelForm


def role_list(request):
    role_queryset = models.Role.objects.all()
    return render(request, 'rbac/role_list.html', {"roles": role_queryset})


def role_add(request):
    if request.method == "GET":
        form = RoleModelForm()
        return render(request, "rbac/change.html", {"form": form})
    form = RoleModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))
    return render(request, "rbac/change.html", {"form": form})


def role_edit(request, pk):
    role_obj = models.Role.objects.filter(pk=pk).first()
    if not role_obj:
        return HttpResponse('角色不存在')

    if request.method == 'POST':
        form = RoleModelForm(request.POST, instance=role_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:role_list'))
        return render(request, 'rbac/change.html', {"form": form})
    form = RoleModelForm(instance=role_obj) # GET 请求instance 携带默认的值
    return render(request, 'rbac/change.html', {"form": form})


def role_del(request,pk):
    # 很多页面都会有取消的跳转，起一个共有的名字，传给模板，这样模板中每次用同一个名字即可返回各自的起始页面
    cancel_url = reverse('rbac:role_list')
    role_queryset = models.Role.objects.filter(pk=pk)
    if not role_queryset:
        return HttpResponse('角色不存在！')

    if request.method == 'POST':
        role_queryset.delete()
        return redirect(cancel_url)

    return render(request, 'rbac/delete.html', locals())