# Generated by Django 2.0.9 on 2018-11-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_field',
            name='field',
        ),
        migrations.AddField(
            model_name='game_field',
            name='board',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game_field',
            name='room_url',
            field=models.CharField(default='room_url', max_length=100),
        ),
        migrations.AlterField(
            model_name='game_field',
            name='player1',
            field=models.CharField(default='player1', max_length=20),
        ),
        migrations.AlterField(
            model_name='game_field',
            name='player2',
            field=models.CharField(default='player2', max_length=20),
        ),
    ]
