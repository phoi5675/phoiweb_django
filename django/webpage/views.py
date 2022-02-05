from django.conf import settings
from django.http import Http404, HttpResponse 

from .models import *


def index(request): 
    return HttpResponse("Hello, world. You're at the webpage index.")

def boards(request, board_name: str) -> HttpResponse:
    query = Board.objects.filter(name=board_name).values()

    return HttpResponse(query, content_type='application/json')

def article_image(request, title: str, img: str) -> HttpResponse:
    query = Article.objects.filter(title=title).first()
    article_path = query.file_name
    board_path = query.board_name.storage_path

    
    directory = settings.BOARD_DIR + board_path + article_path + '/' + 'img/'
    print('directory : ' + directory)
    try:
        with open(directory + img, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')
    except FileNotFoundError:
        raise Http404("File not found!")