from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from pprint import pprint

User = get_user_model()


class RegisterViewTest(TestCase):
    def setUp(self):
        self.url = reverse("users:register")
        self.username = "user"
        self.first_name = "Пользователь"
        self.password = "1234"

    def test_view_by_url(self):
        response = self.client.get("/users/register/")
        self.assertEqual(response.status_code, 200)

    def test_view_by_url_name(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_valid_register(self):
        response = self.client.post(
            self.url,
            data={
                "username": self.username,
                "first_name": self.first_name,
                "password1": self.password,
                "password2": self.password,
            },
        )
        self.assertRedirects(response, reverse("home"))

        user = User.objects.get(username=self.username)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.first_name, self.first_name)
        self.assertTrue(user.check_password(self.password))

    def test_register_different_passwords(self):
        response = self.client.post(
            self.url,
            data={
                "username": self.username,
                "first_name": self.first_name,
                "password1": self.password,
                "password2": self.first_name,
            },
        )
        self.assertContains(response, "Введенные пароли не совпадают.", status_code=200)

        self.assertTrue(response.context["form"].errors)
        self.assertEqual(
            response.context["form"].errors["password2"],
            ["Введенные пароли не совпадают."],
        )

    def test_register_without_username(self):
        response = self.client.post(
            self.url,
            data={
                "first_name": self.first_name,
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertContains(response, "Обязательное поле.", status_code=200)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(
            response.context["form"].errors["username"], ["Обязательное поле."]
        )

    def test_register_without_first_name(self):
        response = self.client.post(
            self.url,
            data={
                "username": self.username,
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertContains(response, "Обязательное поле.", status_code=200)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(
            response.context["form"].errors["first_name"], ["Обязательное поле."]
        )

    def test_register_without_password1(self):
        response = self.client.post(
            self.url,
            data={
                "username": self.username,
                "first_name": self.first_name,
                "password2": self.password,
            },
        )

        self.assertContains(response, "Обязательное поле.", status_code=200)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(
            response.context["form"].errors["password1"], ["Обязательное поле."]
        )

    def test_register_without_password2(self):
        response = self.client.post(
            self.url,
            data={
                "username": self.username,
                "first_name": self.first_name,
                "password1": self.password,
            },
        )

        self.assertContains(response, "Обязательное поле.", status_code=200)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(
            response.context["form"].errors["password2"], ["Обязательное поле."]
        )

    def test_register_existing_username(self):
        User.objects.create_user(
            username=self.username, password=self.password, first_name=self.first_name
        )
        response = self.client.post(
            self.url,
            data={
                "username": self.username,
                "first_name": self.first_name,
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertContains(
            response, "Пользователь с таким Логин уже существует.", status_code=200
        )
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(
            response.context["form"].errors["username"],
            ["Пользователь с таким Логин уже существует."],
        )
