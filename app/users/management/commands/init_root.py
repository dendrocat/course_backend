from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    __username = "root"
    __password = "1234"

    help = f"Create superuser with username={__username} and password={__password}"

    def handle(self, *args, **options):
        if not User.objects.filter(username=self.__username).exists():
            root = User.objects.create(
                username=self.__username, password=make_password(self.__password)
            )
            root.is_active = True
            root.is_staff = True
            root.is_superuser = True
            root.save()
            print(f'Superuser with username "{self.__username}" created succesfully')
        else:
            print(
                f'Superuser with username "{self.__username}" has already been created'
            )
