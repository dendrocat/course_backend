from django.apps import AppConfig


class GameConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "game"
    verbose_name = "Игровые данные"

    def ready(self):
        import game.signals

        return super().ready()
