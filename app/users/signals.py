from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from game.models import GameData


@receiver(post_save, sender=get_user_model())
def create_gamedata(sender, instance, created, **kwargs):
    if created:
        GameData.objects.create(user=instance)
