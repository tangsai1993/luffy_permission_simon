# -*- encoding: utf-8 -*-
"""
@File    : url_filter.py
@Time    : 2021-12-26 21:33
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from django.http import QueryDict
from django.urls import reverse


def memory_url(request, name, *args, **kwargs):
    """
    打包转义带有请求参数的URL
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


def memory_reverse(request, name, *args, **kwargs):
    """
    先反向生成之前页面的原生url，再与当前页面的get请求参数拼接组成新的url，
    即可跳转回之前的页面
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """
    url = reverse(name, args=args, kwargs=kwargs)
    if request.GET:
        menu_id = request.GET.get('_filter')
        url += '?{}'.format(menu_id)
    return url
