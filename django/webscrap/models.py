# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Major(models.Model):
    school = models.ForeignKey('School', models.DO_NOTHING, db_column='school')
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'major'
        app_label = 'webscrap'


class School(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    code = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = True
        db_table = 'school'
        app_label = 'webscrap'


class Subscriber(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    registered_date = models.DateTimeField()
    school = models.ForeignKey(School, models.DO_NOTHING, db_column='school')
    major = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'subscriber'
        app_label = 'webscrap'


class UrlTable(models.Model):
    school = models.CharField(max_length=100)
    url = models.TextField(unique=True)
    additional_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'url_table'
        app_label = 'webscrap'
