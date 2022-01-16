#! -*- coding:utf-8 -*-
from django import forms
from django.forms.widgets import TextInput

from rbac import models


class RoleModelForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = ["title", ]
        error_messages = {
            'title': {'required': '角色名称不能为空！'}
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'})
        }
