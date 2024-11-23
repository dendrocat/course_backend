from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class GameData(models.Model):
    money = models.IntegerField(verbose_name="Монеты", default=0, blank=False)
    height = models.IntegerField(verbose_name="Высота", default=0, blank=False)
    width = models.IntegerField(verbose_name="Ширина", default=0, blank=False)
    level = models.IntegerField(verbose_name="Уровень", default=1, blank=False)
    user = models.OneToOneField(
        get_user_model(),
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        blank=False,
        related_name="gamedata",
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Игровые данные"
        verbose_name_plural = "Игровые данные"
        ordering = ["-level", "-money", "-height", "-width", "user"]

    def __str__(self):
        return f"{self.user.username}: {self.level} level, {self.money} money"
