# -*- encoding: utf-8 -*-
"""
@File    : menu.py
@Time    : 2021-12-26 21:31
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from django import forms
from django.utils.safestring import mark_safe
from rbac import models

from rbac.forms.base import BootStrapModelForm
from rbac.models import Menu, Permission


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['title', 'icon']
        widgets = {
            'title': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.RadioSelect(
                choices=[
                    # 第一个元素为checkbox的值，第二个元素为value
                    ('fa-address-book', mark_safe('<i class="fa fa-address-book" aria-hidden="true"></i>')),
                    ('fa-meetup', mark_safe('<i class="fa fa-meetup" aria-hidden="true"></i>')),
                    ('fa-microchip', mark_safe('<i class="fa fa-microchip" aria-hidden="true"></i>')),
                    ('fa-shower', mark_safe('<i class="fa fa-shower" aria-hidden="true"></i>')),
                    ('fa-thermometer-three-quarters',
                     mark_safe('<i class="fa fa-thermometer-three-quarters" aria-hidden="true"></i>')),
                    ('fa-address-card', mark_safe('<i class="fa fa-address-card" aria-hidden="true"></i>')),
                    ('fa-handshake-o', mark_safe('<i class="fa fa-handshake-o" aria-hidden="true"></i>')),
                    ('fa-eercast', mark_safe('<i class="fa fa-eercast" aria-hidden="true"></i>')),
                    ('fa-free-code-camp', mark_safe('<i class="fa fa-free-code-camp" aria-hidden="true"></i>')),
                    ('fa-grav', mark_safe('<i class="fa fa-grav" aria-hidden="true"></i>')),
                    ('fa-podcast', mark_safe('<i class="fa fa-podcast" aria-hidden="true"></i>')),
                    ('fa-snowflake-o', mark_safe('<i class="fa fa-snowflake-o" aria-hidden="true"></i>')),
                    ('fa-superpowers', mark_safe('<i class="fa fa-superpowers" aria-hidden="true"></i>')),
                    ('fa-wpexplorer', mark_safe('<i class="fa fa-wpexplorer" aria-hidden="true"></i>')),
                    ('fa-gitlab', mark_safe('<i class="fa fa-gitlab" aria-hidden="true"></i>')),
                    ('fa-question-circle-o', mark_safe('<i class="fa fa-question-circle-o" aria-hidden="true"></i>')),
                    ('fa-window-close', mark_safe('<i class="fa fa-window-close" aria-hidden="true"></i>')),
                ],
            )
        }


class SecondMenuModelForm(BootStrapModelForm):
    menu = forms.models.ModelChoiceField(
        queryset=Menu.objects.all(),
        label='所属菜单',
        initial=0,
        required=True,
        error_messages={'required': '请选择一个一级菜单'}
    )

    class Meta:
        model = Permission
        exclude = ['pid']


class PermissionModelForm(BootStrapModelForm):
    class Meta:
        model = Permission
        fields = ['title', 'name', 'url']


class MultiPermissionModelForm(BootStrapModelForm):
    class Meta:
        model = Permission
        fields = '__all__'


class MultiUpdatePermissionModelForm(forms.Form):
    # HiddenInput隐藏input标签
    id = forms.IntegerField(label='id', widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    url = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    menu_id = forms.ChoiceField(choices=[(None, '-----')],
                                widget=forms.widgets.Select(attrs={'class': 'form-control'}),
                                required=False,
                                )
    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.widgets.Select(attrs={'class': 'form-control'}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += Permission.objects.filter(pid__isnull=True, menu__isnull=False).values_list(
            'id', 'title')


class MultiAddPermissionForm(forms.Form):
    title = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    url = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    menu_id = forms.ChoiceField(choices=[(None, '-----')],
                                widget=forms.widgets.Select(attrs={'class': 'form-control'}),
                                required=False,
                                )
    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.widgets.Select(attrs={'class': 'form-control'}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += Permission.objects.filter(pid__isnull=True, menu__isnull=False).values_list(
            'id', 'title')


class MultiEditPermissionForm(forms.Form):
    id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,

    )

    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')