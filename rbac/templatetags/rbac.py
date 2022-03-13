#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.template import Library
from django.conf import settings
from collections import OrderedDict
from rbac.service import urls

register = Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    """
    创建一级菜单
    :return:
    """
    menu_list = request.session[settings.MENU_SESSION_KEY]
    return {'menu_list': menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    """
    创建二级菜单
    :return:
    """
    menu_dict = request.session[settings.MENU_SESSION_KEY]

    # 对字典的key进行排序
    key_list = sorted(menu_dict)

    # 空的有序字典
    ordered_dict = OrderedDict()

    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'

        for per in val['children']:
            if per['id'] == request.current_selected_permission:
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val

    return {'menu_dict': ordered_dict}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
    return {'record_list': request.breadcrumb}


@register.filter
def has_permission(request, name):
    """
    判断是否有权限
    :param request:
    :param name:
    :return:
    """
    if name in request.session[settings.PERMISSION_SESSION_KEY]:
        return True

@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    """
    打包转义带有请求参数的URL  返回到原来的页面 之前的参数也要携带着
    :param request:
    :param name: url别名
    :return:
    """

    return urls.memory_url(request, name, *args, **kwargs)