# Generated by Django 5.1.3 on 2024-11-18 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamedata',
            options={'ordering': ['-level', '-money', '-height', '-width', 'user'], 'verbose_name': 'Игровые данные', 'verbose_name_plural': 'Игровые данные'},
        ),
    ]