# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    : 2021-12-26 12:59
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from django import forms
from django.core.exceptions import ValidationError
from rbac import models


class UserModelForm(forms.ModelForm):
    # 添加额外字段
    confirm_password = forms.CharField(label="确认密码")

    class Meta:
        model = models.UserInfo
        fields = ["name", "email", "password", "confirm_password"]
        # 在settings.py中设置LANGUAGE_CODE = 'zh-hans'，即可自动将错误提示转为中文
        # error_messages = {
        #     'name':{'required':'用户名不能为空！'},
        #     'email':{'required':'邮箱不能为空！'},
        #     'password':{'required':'密码不能为空！'},
        # }

    # 循环为每一个字段添加样式
    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    # 局部钩子，检验两次密码是否一致
    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            raise ValidationError("两次密码不一致！")
        return confirm_password


class UpdateUserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "email"]

    def __init__(self, *args, **kwargs):
        super(UpdateUserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ResetPasswordModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_pwd(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password == confirm_password:
                return self.cleaned_data
            raise ValidationError('两次密码不一致！')
        else:
            return self.cleaned_data
