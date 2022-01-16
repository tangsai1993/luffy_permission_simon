from django.contrib import admin

# Register your models here.
from rbac import models
# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.Permission)
admin.site.register(models.Role)