# Generated by Django 4.1.2 on 2022-11-05 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reitngstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]
