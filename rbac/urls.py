#! -*- coding:utf-8 -*-
from django.urls import path, re_path
from rbac.views import role, user, menu

app_name = 'rbac'
urlpatterns = [
    path(r"role/list/", role.role_list, name="role_list"),
    path(r"role/add/", role.role_add, name="role_add"),
    re_path(r"^role/edit/(?P<pk>\d+)/$", role.role_edit, name="role_edit"),
    re_path(r"^role/del/(?P<pk>\d+)/$", role.role_del, name="role_del"),

    path(r"user/list/", user.user_list, name="user_list"),
    path(r"user/add/", user.user_add, name="user_add"),
    re_path(r"^user/edit/(?P<pk>\d+)/$", user.user_edit, name="user_edit"),
    re_path(r"^user/del/(?P<pk>\d+)/$", user.user_del, name="user_del"),
    re_path(r"^user/reset/password/(?P<pk>\d+)/$", user.user_reset_pwd, name="user_reset_pwd"),

    path("menu/list/", menu.menu_list, name="menu_list"),
    path('menu/add/', menu.menu_add, name='menu_add'),
    re_path('^menu/eidt/(?P<pk>\d+)/$', menu.menu_edit, name='menu_edit'),
    re_path('^menu/del/(?P<pk>\d+)/$', menu.menu_del, name='menu_del'),

    re_path('^second/menu/add/(?P<menu_id>\d+)/$', menu.second_menu_add, name='second_menu_add'),
    re_path('^second/menu/eidt/(?P<pk>\d+)/$', menu.second_menu_edit, name='second_menu_edit'),
    re_path('^second/menu/del/(?P<pk>\d+)/$', menu.second_menu_del, name='second_menu_del'),

    re_path('^permission/add/(?P<second_menu_id>\d+)/$', menu.permission_add, name='permission_add'),
    re_path('^permission/edit/(?P<pk>\d+)/$', menu.permission_edit, name='permission_edit'),
    re_path('^permission/del/(?P<pk>\d+)/$', menu.permission_del, name='permission_del'),

    path('multi/permissions/', menu.multi_permissions, name='multi_permissions'),
    re_path('^multi_permissions/del/(?P<pk>\d+)/$', menu.multi_permissions_del, name='multi_permissions_del'),

    re_path(r'^distribute/permissions/$', menu.distribute_permissions, name='distribute_permissions'),

]
