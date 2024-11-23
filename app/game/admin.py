from urllib.parse import urlencode
from django.urls import reverse

from django.contrib import admin
from django.utils.html import format_html
from .models import GameData


# Register your models here.
@admin.register(GameData)
class GameDataConfig(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        return GameData.objects.all().select_related("user")

    list_display = (
        "view_user_link",
        "level",
        "money",
        "height",
        "width",
        "change_link",
    )
    readonly_fields = ["user"]

    def view_user_link(self, obj):
        # Формируем правильный URL для страницы списка пользователей в админке
        url = reverse("admin:users_user_change", args=[obj.user.id])  # Фильтрация по ID

        # Возвращаем HTML ссылку
        return format_html(f'<a href="{url}">{obj.user.username}</a>')

    view_user_link.short_description = "Пользователь"

    def change_link(self, obj):
        url = reverse("admin:game_gamedata_change", args=[obj.id])
        return format_html(f'<a href="{url}">Изменить</a>')

    change_link.short_description = "Ссылки"

    fieldsets = [
        ("Пользователь", {"fields": ["user"]}),
        ("Данные", {"fields": ["level", "money", "height", "width"]}),
    ]

    add_fieldsets = [
        ("Пользователь", {"fields": ["user"]}),
        ("Данные", {"fields": ["level", "money", "height", "width"]}),
    ]
