from django.urls import path
from blog_backend import api

urlpatterns = [
    path('add-article/',api.add_article)

]