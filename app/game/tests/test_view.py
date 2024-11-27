from urllib.parse import urlencode
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()


class GameViewTest(TestCase):
    def setUp(self):
        self.username = "user"
        self.password = "1234"
        self.user = User.objects.create_user(
            username="user", first_name="user", password="1234"
        )

    def test_game_view_by_url(self):
        response = self.client.get("/game/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/users/login/?next=/game/")

    def test_game_view_by_url_name(self):
        response = self.client.get(reverse("game:index"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("users:login") + "?" + urlencode({"next": reverse("game:index")}),
        )

    def test_game_view_with_auth(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("game:index"))
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_view_by_url_(self):
        response = self.client.get("/game/leaders")
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_view_by_url_name(self):
        response = self.client.get(reverse("game:leaderboard"))
        self.assertEqual(response.status_code, 200)

    def test_api_view_by_url_no_auth(self):
        response = self.client.get("/game/api")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_view_by_url_(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get("/game/api")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_view_with_auth(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_view_get(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_view_patch(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.patch(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_view_post(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_api_view_put(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.put(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_api_view_delete(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.delete(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
