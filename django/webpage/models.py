# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    board_name = models.ForeignKey('Board', models.DO_NOTHING, db_column='board_name', default='board')
    file_name = models.TextField()
    preview_text = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self): 
        return f'{self.id}|{self.title}|{self.file_name}|{self.board_name}'

    class Meta:
        managed = True
        db_table = 'article'
        app_label = 'webpage'

class Board(models.Model):
    id = models.IntegerField()
    name = models.TextField(primary_key=True)
    storage_path = models.TextField(unique=True)

    def __str__(self) -> str:
        return f'{self.id}|{self.name}|{self.storage_path}'
        
    class Meta:
        managed = True
        db_table = 'board'
        app_label = 'webpage'
