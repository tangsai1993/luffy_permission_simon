# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    : 2021-12-26 12:58
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django import forms
from django.forms.widgets import TextInput

from rbac import models
from rbac.forms.user import UserModelForm, UpdateUserModelForm, ResetPasswordModelForm


def user_list(request):
    user_queryset = models.UserInfo.objects.all()
    return render(request, 'rbac/user_list.html', {"users": user_queryset})


def user_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "rbac/change.html", {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))
    return render(request, "rbac/change.html", {"form": form})


def user_edit(request, pk):
    user_obj = models.UserInfo.objects.filter(pk=pk).first()
    if not user_obj:
        return HttpResponse('用户不存在')

    if request.method == 'POST':
        form = UpdateUserModelForm(data=request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:user_list'))
        return render(request, 'rbac/change.html', {"form": form})
    form = UpdateUserModelForm(instance=user_obj)  # GET 请求instance 携带默认的值
    return render(request, 'rbac/change.html', {"form": form})


def user_del(request, pk):
    # 很多页面都会有取消的跳转，起一个共有的名字，传给模板，这样模板中每次用同一个名字即可返回各自的起始页面
    cancel_url = reverse('rbac:user_list')
    user_queryset = models.UserInfo.objects.filter(pk=pk)
    if not user_queryset:
        return HttpResponse('角色不存在！')

    if request.method == 'POST':
        user_queryset.delete()
        return redirect(cancel_url)

    return render(request, 'rbac/delete.html', locals())


def user_reset_pwd(request, pk):
    user_obj = models.UserInfo.objects.filter(pk=pk).first()
    if not user_obj:
        return HttpResponse('角色不存在')

    if request.method == 'POST':
        form = ResetPasswordModelForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:user_list'))
        return render(request, 'rbac/change.html',  {"form": form})

    form = ResetPasswordModelForm()
    return render(request, 'rbac/change.html',  {"form": form})
