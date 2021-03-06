# Generated by Django 4.0.1 on 2022-02-05 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('storage_path', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'board',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('file_name', models.TextField()),
                ('preview_text', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField()),
                ('board_name', models.ForeignKey(db_column='board_name', default='board', on_delete=django.db.models.deletion.DO_NOTHING, to='webpage.board')),
            ],
            options={
                'db_table': 'article',
                'managed': True,
            },
        ),
    ]
