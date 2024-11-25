from django.test import TestCase
from users.forms import RegisterForm


class RegisterFormText(TestCase):
    def test_valid(self):
        data = {
            "login": "user3",
            "username": "Пользователь",
            "password1": "1234",
            "password2": "1234",
        }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_without_login(self):
        data = {
            "username": "Пользователь",
            "password1": "1234",
            "password2": "1234",
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())

    def test_without_username(self):
        data = {
            "login": "user3",
            "password1": "1234",
            "password2": "1234",
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())

    def test_different_password(self):
        data = {
            "login": "user3",
            "username": "Пользователь",
            "password1": "1234",
            "password2": "password",
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
