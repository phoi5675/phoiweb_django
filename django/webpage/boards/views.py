import mimetypes
from django.core import serializers
from django.conf import settings
from django.http import Http404, HttpResponse 
from PIL import Image

from ..models import *

def boards(request) -> HttpResponse:
    query = Board.objects.all()
    data = serializers.serialize('json', query)

    return HttpResponse(data, content_type='application/json')

def articles(request, board_name: str) -> HttpResponse:
    query = Article.objects.filter(board_name=board_name)
    data = serializers.serialize('json', query)

    return HttpResponse(data, content_type='application/json')
