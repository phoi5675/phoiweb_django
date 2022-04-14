import mimetypes
from django.core import serializers
from django.conf import settings
from django.http import Http404, HttpResponse 
from PIL import Image

from .models import *


def index(request): 
    return HttpResponse("Hello, world. You're at the webpage index.")
