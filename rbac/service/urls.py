# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2021-12-26 21:34
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from django.urls import reverse
from django.http import QueryDict


def memory_reverse_url(request, name, *args, **kwargs):
    """
    反向生成url：
        http://127.0.0.1:8000/rbac/menu/add?_filter=mid%3D1
        在url中将原来的搜索条件，如_filter后面的值
        reverse生成原来的url，如/menu/add/
        menu/add?mid%3D1
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    # url = reverse("rbac:menu_list", args=args, kwargs=kwargs)
    url = reverse(name, args=args, kwargs=kwargs)
    origin_params = request.GET.get("_filter")
    if origin_params:
        url = "%s?%s" % (url, origin_params)
    return url


def memory_url(request, name, *args, **kwargs):
    """
    打包转义带有请求参数的URL  返回到原来的页面 之前的参数也要携带着
    :param request:
    :param name: url别名
    :return:
    """
    # 原生url
    url = reverse(name, args=args, kwargs=kwargs)
    # 有get参数才返回参数
    if request.GET:
        query_dict = QueryDict(mutable=True)
        query_dict['_filter'] = request.GET.urlencode()
        # 带get请求参数的转义url
        url = '{0}?{1}'.format(url, query_dict.urlencode())
    return url
