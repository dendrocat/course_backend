from django.test import TestCase
from users.forms import RegisterForm


class RegisterFormTest(TestCase):
    def setUp(self):
        self.username = "user"
        self.first_name = "Пользователь"
        self.password = "1234"

    def test_valid(self):
        data = {
            "username": self.username,
            "first_name": self.first_name,
            "password1": self.password,
            "password2": self.password,
        }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_without_username(self):
        data = {
            "first_name": self.first_name,
            "password1": self.password,
            "password2": self.password,
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())

    def test_without_first_name(self):
        data = {
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())

    def test_different_password(self):
        data = {
            "username": self.username,
            "first_name": self.first_name,
            "password1": self.password,
            "password2": "password",
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
