from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    file_path = models.ForeignKey('Board', models.DO_NOTHING, db_column='file_path')
    file_name = models.TextField()
    date = models.DateTimeField()
    preview_text = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'article'


class Board(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    local_path = models.TextField(unique=True)
    url = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'board'
