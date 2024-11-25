from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


# Create your tests here.
class UserTest(TestCase):
    def test_create_user(self):
        username = "user"
        first_name = "Пользователь"
        password = "1234"
        user = User.objects.create_user(
            username=username, first_name=first_name, password=password
        )
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, first_name)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        username = "root"
        first_name = "Суперпользователь"
        password = "1234"
        user = User.objects.create_superuser(
            username=username, first_name=first_name, password=password
        )
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, first_name)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_without_first_name(self):
        username = "user"
        password = "1234"
        with self.assertRaises(ValidationError):
            User.objects.create_user(username=username, password=password)
