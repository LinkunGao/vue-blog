from django.urls import path
from blog_backend import api

urlpatterns = [
    path('add-article/',api.add_article),
    # 用户管理
    # 登陆
    path('skycoco-login/', api.skycoco_login),
    # 注册
    path('skycoco-register/', api.skycoco_register),

]