from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    username = "user"
    password = "1234"

    help = f"Create superuser with login={username} and password={password}"

    def handle(self, *args, **options):
        if not User.objects.filter(username=self.username).exists():
            User.objects.create_user(
                username=self.username, password=self.password, first_name=self.username
            )
            print(f'Superuser with username "{self.username}" created succesfully')
        else:
            print(f'Superuser with username "{self.username}" has already been created')
