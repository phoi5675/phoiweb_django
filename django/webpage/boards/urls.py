from urllib.parse import urlparse
from django.urls import path
from . import views


board_urlpatterns = [
    path('', views.boards, name='boards'),
    path('<str:board_name>/articles', views.articles, name='articles'),
]