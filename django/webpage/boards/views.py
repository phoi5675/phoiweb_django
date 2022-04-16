import mimetypes
from django.core import serializers
from django.conf import settings
from django.http import Http404, HttpResponse

import os
from datetime import datetime


from ..models import *

def boards(request) -> HttpResponse:
    query = Board.objects.all()
    data = serializers.serialize('json', query)

    return HttpResponse(data, content_type='application/json')

def articles(request, board_name: str) -> HttpResponse:
    # print('dir : ')
    # dir = os.listdir(settings.BOARD_DIR + board_name)
    # for sub_dir in dir:
    #     path = f'{settings.BOARD_DIR}{board_name}/{sub_dir}'
    #     stat = os.stat(path)
    #     try:
    #         print(f'created date : {datetime.utcfromtimestamp(int(stat.st_birthtime))}')
    #     except AttributeError:
    #         print(f'last modified : {datetime.utcfromtimestamp(int(stat.st_mtime))}')
    
    query = Article.objects.filter(board_name=board_name)
    data = serializers.serialize('json', query)

    return HttpResponse(data, content_type='application/json')
