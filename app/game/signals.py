from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import GameData


@receiver(post_delete, sender=GameData)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()
