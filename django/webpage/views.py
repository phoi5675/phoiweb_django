import mimetypes
from django.core import serializers
from django.conf import settings
from django.http import Http404, HttpResponse 
from PIL import Image

from .models import *


def index(request): 
    return HttpResponse("Hello, world. You're at the webpage index.")

def boards(request) -> HttpResponse:
    query = Board.objects.all()
    data = serializers.serialize('json', query)
    return HttpResponse(data, content_type='application/json')

def articles(request, board_name: str) -> HttpResponse:
    query = Article.objects.filter(board_name=board_name)
    data = serializers.serialize('json', query)
    return HttpResponse(data, content_type='application/json')
    
def article_markdown(request, board: str, title: str) -> HttpResponse:
    query = Article.objects.filter(title=title).first()
    article_path = query.file_name
    board_path = query.board_name.storage_path

    markdown = settings.BOARD_DIR + board_path + article_path + '/markdown.md'
    try:
        with open(markdown, 'r') as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        raise Http404('File not found!')

def article_image(request, board: str, title: str, img: str) -> HttpResponse:
    query = Article.objects.filter(title=title).first()
    article_path = query.file_name
    board_path = query.board_name.storage_path

    directory = settings.BOARD_DIR + board_path + article_path + '/' + 'img/'
    try:
        MAX_IMG_SIZE = (500, 500)
        img: Image = Image.open(directory + img)
        img.thumbnail(MAX_IMG_SIZE)

        response = HttpResponse(content_type='image/jpeg')
        img.save(response, "JPEG")

        return response
    except FileNotFoundError:
        raise Http404('File not found!')
    except OSError as e:
        raise Http404('Error during handling image')

def article_attachment(request, board: str, title: str, attachment: str) -> HttpResponse:
    query = Article.objects.filter(title=title).first()
    article_path = query.file_name
    board_path = query.board_name.storage_path

    directory = settings.BOARD_DIR + board_path + article_path + '/' + 'attachments/'
    try:
        with open(directory + attachment, 'rb') as f:
            mime_type, _ = mimetypes.guess_type(attachment)
            return HttpResponse(f.read(), content_type=mime_type)
    except FileNotFoundError:
        raise Http404('File not found!')