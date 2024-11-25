from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from game.models import GameData

User = get_user_model()


class GameAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("game:api")
        self.username = "user"
        self.password = "1234"
        self.user = User.objects.create_user(
            username=self.username, first_name=self.username, password=self.password
        )

    def test_api_view_by_url_(self):
        response = self.client.get("/game/api")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_view_by_url_name(self):
        response = self.client.get(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_view_with_auth(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("game:api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_data = self.user.gamedata

        self.assertTrue(response.data)
        self.assertEqual(user_data.money, response.data["money"])
        self.assertEqual(user_data.height, response.data["height"])
        self.assertEqual(user_data.width, response.data["width"])
        self.assertEqual(user_data.level, response.data["level"])

    def test_play(self):
        money = 2000
        level = self.user.gamedata.level + 1
        height = 100
        width = 200

        self.client.login(username=self.username, password=self.password)
        response = self.client.patch(
            self.url,
            data={
                "money": money,
                "level": level,
                "height": height,
                "width": width,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

        data = GameData.objects.get(user=self.user)
        self.assertTrue("money" in response.data)
        self.assertEqual(data.money, response.data["money"])
        self.assertEqual(money, response.data["money"])

        self.assertTrue("level" in response.data)
        self.assertEqual(level, response.data["level"])
        self.assertEqual(data.level, response.data["level"])

        self.assertTrue("height" in response.data)
        self.assertEqual(height, response.data["height"])
        self.assertEqual(data.height, response.data["height"])

        self.assertTrue("width" in response.data)
        self.assertEqual(width, response.data["width"])
        self.assertEqual(data.width, response.data["width"])

    def test_wasted(self):
        level = self.user.gamedata.level
        money = 1000
        height = 150
        width = 0

        self.client.login(username=self.username, password=self.password)
        response = self.client.patch(
            self.url, data={"money": money, "height": height, "width": width}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

        data = GameData.objects.get(user=self.user)
        self.assertTrue("money" in response.data)
        self.assertEqual(money, response.data["money"])
        self.assertEqual(data.money, response.data["money"])

        self.assertTrue("level" in response.data)
        self.assertEqual(level, response.data["level"])
        self.assertEqual(data.level, response.data["level"])

        self.assertTrue("height" in response.data)
        self.assertEqual(height, response.data["height"])
        self.assertEqual(data.height, response.data["height"])

        self.assertTrue("width" in response.data)
        self.assertEqual(width, response.data["width"])
        self.assertEqual(data.width, response.data["width"])

    def test_buy_height(self):
        money = 2000
        dm = 150
        height = 0
        dh = 150
        level = self.user.gamedata.level
        width = self.user.gamedata.width

        self.client.login(username=self.username, password=self.password)
        response = self.client.patch(
            self.url, data={"money": money - dm, "height": height + dh}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

        data = GameData.objects.get(user=self.user)
        self.assertTrue("money" in response.data)
        self.assertEqual(money - dm, response.data["money"])
        self.assertEqual(data.money, response.data["money"])

        self.assertTrue("level" in response.data)
        self.assertEqual(level, response.data["level"])
        self.assertEqual(data.level, response.data["level"])

        self.assertTrue("height" in response.data)
        self.assertEqual(height + dh, response.data["height"])
        self.assertEqual(data.height, response.data["height"])

        self.assertTrue("width" in response.data)
        self.assertEqual(width, response.data["width"])
        self.assertEqual(data.width, response.data["width"])

    def test_buy_width(self):
        money = 2000
        dm = 150
        width = 0
        dw = 150
        level = self.user.gamedata.level
        height = self.user.gamedata.height

        self.client.login(username=self.username, password=self.password)
        response = self.client.patch(
            self.url, data={"money": money - dm, "width": width + dw}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        data = GameData.objects.get(user=self.user)
        self.assertTrue("money" in response.data)
        self.assertEqual(money - dm, response.data["money"])
        self.assertEqual(data.money, response.data["money"])

        self.assertTrue("level" in response.data)
        self.assertEqual(level, response.data["level"])
        self.assertEqual(data.level, response.data["level"])

        self.assertTrue("height" in response.data)
        self.assertEqual(height, response.data["height"])
        self.assertEqual(data.height, response.data["height"])

        self.assertTrue("width" in response.data)
        self.assertEqual(width + dw, response.data["width"])
        self.assertEqual(data.width, response.data["width"])

    def test_patch_wrong(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.patch(
            self.url,
            data={"wrongkey": "somedata"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
