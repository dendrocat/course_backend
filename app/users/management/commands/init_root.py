from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    login = "root"
    password = "1234"

    help = f"Create superuser with login={login} and password={password}"

    def handle(self, *args, **options):
        if not User.objects.filter(login=self.login).exists():
            User.objects.create_superuser(login=self.login, password=self.password)
            print(f'Superuser with login "{self.login}" created succesfully')
        else:
            print(f'Superuser with username "{self.login}" has already been created')
