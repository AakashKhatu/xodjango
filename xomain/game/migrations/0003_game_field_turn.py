# Generated by Django 2.0.9 on 2018-11-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20181124_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_field',
            name='turn',
            field=models.IntegerField(default=0),
        ),
    ]
