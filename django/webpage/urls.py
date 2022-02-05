from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boards/', views.boards, name='boardss'),
    path('article/<str:title>/<str:img>', views.article_image, name='article_image')
]