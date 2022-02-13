from django.contrib import admin

# Register your models here.
from .models import Article, Board

admin.site.register(Article)
admin.site.register(Board)