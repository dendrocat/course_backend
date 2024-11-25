from django.test import TestCase
from django.contrib.auth import get_user_model
from game.models import GameData

User = get_user_model()


class GameDataModelTest(TestCase):
    def setUp(self):
        self.username = "user"
        self.password = "1234"

    def create_user(self):
        user = User.objects.create_user(
            username=self.username, first_name=self.username, password=self.password
        )
        return user

    def test_create(self):
        user = self.create_user()

        data = GameData.objects.get(user=user)
        self.assertIsNotNone(data)
        self.assertEqual(data.user, user)
        self.assertEqual(data.money, 0)
        self.assertEqual(data.height, 0)
        self.assertEqual(data.width, 0)
        self.assertEqual(data.level, 1)

    def test_delete_data(self):
        user = self.create_user()
        data = user.gamedata
        data.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=user.pk)

    def test_delete_user(self):
        user = self.create_user()
        pk = user.gamedata.pk
        user.delete()

        with self.assertRaises(GameData.DoesNotExist):
            GameData.objects.get(pk=pk)
