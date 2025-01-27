from rest_framework import serializers
from .models import GameData


class GameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameData
        fields = ["money", "height", "width", "level"]
