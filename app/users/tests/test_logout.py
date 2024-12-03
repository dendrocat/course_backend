from django.test import TestCase
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

User = get_user_model()


class LogoutViewTests(TestCase):
    def setUp(self):
        self.url = reverse("users:login")
        self.username = "user"
        self.first_name = "Пользователь"
        self.password = "1234"

        User.objects.create_user(
            username=self.username, password=self.password, first_name=self.first_name
        )

    def test_get_view_by_url(self):
        response = self.client.get("/users/logout/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_get_view_by_url_name(self):
        response = self.client.get(reverse("users:logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_logout_from_unauthorized(self):
        user = get_user(self.client)
        self.assertIsInstance(user, AnonymousUser)

        response = self.client.get(reverse("users:logout"))

        user = get_user(self.client)
        self.assertIsInstance(user, AnonymousUser)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_logout_from_authorized(self):
        user = get_user(self.client)
        self.assertIsInstance(user, AnonymousUser)

        self.client.login(username=self.username, password=self.password)

        user = get_user(self.client)
        self.assertIsInstance(user, User)

        response = self.client.get(reverse("users:logout"))

        user = get_user(self.client)
        self.assertIsInstance(user, AnonymousUser)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
