# Generated by Django 4.1.1 on 2022-11-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('director_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]