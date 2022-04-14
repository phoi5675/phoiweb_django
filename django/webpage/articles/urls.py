from urllib.parse import urlparse
from django.urls import path, include
from . import views


article_urlpatterns = [
    path('', views.article_markdown, name='article_content'),
    path('img/<str:img>', views.article_image, name='article_image'),
    path('attachments/<str:attachment>', views.article_attachment, name='article_attachment'),
]