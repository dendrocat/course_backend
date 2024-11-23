from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import reverse


model_user = get_user_model()
admin.site.unregister(model_user)

# # Register your models here.
@admin.register(model_user)
class UserConfig(UserAdmin):

    list_display = [
        "username",
        "view_gamedata_link",
        "is_superuser",
        "is_active",
    ]
    list_filter = ["is_superuser"]

    search_fields = ["username"]

    list_display_links = ["username"]

    def view_gamedata_link(self, obj):
        url = reverse("admin:game_gamedata_change", args=[obj.gamedata.id])
        return format_html(f'<a href="{url}">Изменить игровые данные</a>')

    view_gamedata_link.short_description = "Игровые данные"

    fieldsets = [
        ("Данные для входа", {"fields": ["username", "password"]}),
        ("Права доступа", {"fields": ["is_active", "is_superuser"]}),
    ]
