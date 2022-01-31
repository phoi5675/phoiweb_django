from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    code = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'school'


class Major(models.Model):
    school = models.ForeignKey('School', models.DO_NOTHING, db_column='school')
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'major'


class Subscriber(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    registered_date = models.DateTimeField()
    school = models.ForeignKey(School, models.DO_NOTHING, db_column='school')
    major = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subscriber'


class UrlTable(models.Model):
    school = models.CharField(max_length=100)
    url = models.TextField(unique=True)
    additional_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url_table'
