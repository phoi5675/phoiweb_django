from urllib.parse import urlparse
from django.urls import path, include
from . import views

from .boards.urls import board_urlpatterns
from .articles.urls import article_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('boards/', include(board_urlpatterns)),
    path('<str:board>/<str:title>/', include(article_urlpatterns))
]