# -*- encoding: utf-8 -*-
"""
@File    : base.py
@Time    : 2021-12-26 21:32
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from django import forms


class BootStrapModelForm(forms.ModelForm):
    """
    任意的modelform继承该类，可自动为每个字段设置样式
    """

    def __init__(self, *args, **kwargs):
        super(BootStrapModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if 'ModelChoiceField' in field.__repr__():
                field.widget.attrs = {
                    "class": 'form-control selectpicker',
                    'title': '请选择',
                    'data-live-search': 'true',
                    'data-style': 'btn-success',
                }

            if name == 'id':
                self.fields.move_to_end('id', last=False)
