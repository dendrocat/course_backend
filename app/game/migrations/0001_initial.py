# Generated by Django 5.1.3 on 2024-11-18 15:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0, verbose_name='Монеты')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('level', models.IntegerField(default=1, verbose_name='Уровень')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gamedata', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Игровые данные',
                'verbose_name_plural': 'Игровые данные',
            },
        ),
    ]
