# Generated by Django 4.1.1 on 2022-11-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Квентин Тарантино', max_length=100),
        ),
    ]
