from django.contrib import admin
#
# Register your models here.
# 将数据库中的表导入到这里后，才能在admin页面看见
from blog_backend.models import Articles
from blog_backend.models import UserInfo
# 将该表注册到页面
admin.site.register(Articles)
admin.site.register(UserInfo)