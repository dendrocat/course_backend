from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class LoginViewTest(TestCase):
    login = "user"
    username = "Пользователь"
    password = "1234"

    def setUp(self):
        User.objects.create_user(
            login=self.login, username=self.username, password=self.password
        )
        return super().setUp()

    def test_view_by_url(self):
        response = self.client.get("/users/login/")
        self.assertEqual(response.status_code, 200)

    def test_view_by_url_name(self):
        response = self.client.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        response = self.client.post(
            reverse("users:login"),
            data={
                "username": self.login,
                "password": self.password,
            },
        )
        # После успешного входа пользователя должен редиректить на главную страницу
        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        response = self.client.post(
            reverse("users:login"),
            data={
                "username": self.password,  # неправильный логин
                "password": "wrongpassword",
            },
        )
        self.assertContains(
            response,
            "Пожалуйста, введите правильные Логин и пароль. Оба поля могут быть чувствительны к регистру.",
            status_code=200,
        )

        self.assertTrue(response.context["form"].errors)

    def test_invalid_password(self):
        response = self.client.post(
            reverse("users:login"),
            data={
                "username": self.login,
                "password": "wrongpassword",  # неправильный пароль
            },
        )
        self.assertContains(
            response,
            "Пожалуйста, введите правильные Логин и пароль. Оба поля могут быть чувствительны к регистру.",
            status_code=200,
        )

        self.assertTrue(response.context["form"].errors)
