from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import GameData


@receiver(post_save, sender=get_user_model())
def create_gamedata(sender, instance, created, **kwargs):
    if created:
        GameData.objects.create(user=instance)


@receiver(post_delete, sender=GameData)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()
