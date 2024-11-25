from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from urllib.parse import urlencode

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
