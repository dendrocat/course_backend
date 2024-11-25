from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.urls import reverse


admin.site.unregister(Group)

User = get_user_model()


# Register your models here.
@admin.register(User)
class UserConfig(UserAdmin):

    def get_queryset(self, request):
        return User.objects.all().select_related("gamedata")

    list_display = (
        "username",
        "first_name",
        "is_superuser",
        "view_gamedata_link",
    )
    list_display_links = ("username",)
    list_filter = ("is_superuser",)
    search_fields = ("first_name", "username")
    ordering = ("pk",)

    def view_gamedata_link(self, obj):
        url = reverse("admin:game_gamedata_change", args=[obj.gamedata.id])
        return format_html(f'<a href="{url}">Изменить игровые данные</a>')

    view_gamedata_link.short_description = "Игровые данные"

    fieldsets = [
        ("Данные для входа", {"fields": ["username", "password"]}),
        (_("Personal info"), {"fields": ["first_name"]}),
        (_("Permissions"), {"fields": ["is_active", "is_staff", "is_superuser"]}),
    ]

    add_fieldsets = [
        ("Данные для входа", {"fields": ["username", "password1", "password2"]}),
        (_("Personal info"), {"fields": ["first_name"]}),
        (_("Permissions"), {"fields": ["is_active", "is_staff", "is_superuser"]}),
    ]
