from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


# Create your tests here.
class UserTest(TestCase):
    def test_create_user(self):
        login = "user"
        username = "Пользователь"
        password = "1234"
        user = User.objects.create_user(
            login=login, username=username, password=password
        )
        self.assertEqual(user.login, login)
        self.assertEqual(user.username, username)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        login = "root"
        username = "Суперпользователь"
        password = "1234"
        user = User.objects.create_superuser(
            login=login, username=username, password=password
        )
        self.assertEqual(user.login, login)
        self.assertEqual(user.username, username)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_without_username(self):
        login = "user"
        password = "1234"
        with self.assertRaises(ValidationError):
            User.objects.create_user(login=login, password=password)
