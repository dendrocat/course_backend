from django.test import TestCase
from django.contrib.auth import get_user_model
from game.models import GameData

User = get_user_model()


class SortingTest(TestCase):
    def update_gamedata(self, gamedata, money, width, height, level):
        gamedata.money = money
        gamedata.width = width
        gamedata.height = height
        gamedata.level = level
        gamedata.save()

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1", first_name="user1", password="1234"
        )
        self.user2 = User.objects.create_user(
            username="user2", first_name="user2", password="1234"
        )
        self.user3 = User.objects.create_user(
            username="user3", first_name="user3", password="1234"
        )

        self.update_gamedata(self.user1.gamedata, money=50, height=10, width=5, level=3)
        self.update_gamedata(
            self.user2.gamedata, money=100, height=15, width=8, level=2
        )
        self.update_gamedata(
            self.user3.gamedata, money=150, height=12, width=6, level=1
        )

    def test_top(self):
        top = GameData.objects.all()

        for i in range(3):
            self.assertEqual(top[i].user.username, f"user{i+1}")

    def test_update_top(self):
        user4 = User.objects.create_user(
            username="user4", first_name="user4", password="1234"
        )
        self.update_gamedata(user4.gamedata, 49, 5, 20, 3)

        top = GameData.objects.all()

        self.assertEqual(top[0].user.username, "user1")
        self.assertEqual(top[1].user.username, "user4")
        self.assertEqual(top[2].user.username, "user2")
        self.assertEqual(top[3].user.username, "user3")
