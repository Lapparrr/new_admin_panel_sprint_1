# Generated by Django 3.2 on 2023-01-25 19:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('rating', models.FloatField(blank=True, verbose_name='Rating')),
                ('type', models.CharField(blank=True, choices=[('MOV', 'movie'), ('TVS', 'tv_show')], max_length=3, verbose_name='type')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Кино',
                'verbose_name_plural': 'Кино',
                'db_table': 'content"."film_work',
            },
        ),
    ]