from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boards/', views.boards, name='boards'),
    path('article/<str:title>/', views.article_markdown, name='article_content'),
    path('article/<str:title>/images/<str:img>', views.article_image, name='article_image'),
    path('article/<str:title>/attachments/<str:attachment>', views.article_attachment, name='article_attachment')
]