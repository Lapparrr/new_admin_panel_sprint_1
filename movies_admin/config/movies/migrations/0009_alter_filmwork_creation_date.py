# Generated by Django 3.2 on 2023-01-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_filmwork_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(blank=True, verbose_name='Creation_date'),
        ),
    ]