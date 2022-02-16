from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boards/', views.boards, name='boards'),
    path('boards/<str:board_name>/articles', views.articles, name='articles'),
    path('<str:board>/<str:title>/', views.article_markdown, name='article_content'),
    path('<str:board>/<str:title>/img/<str:img>', views.article_image, name='article_image'),
    path('<str:board>/<str:title>/attachments/<str:attachment>', views.article_attachment, name='article_attachment')
]