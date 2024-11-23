from rest_framework import serializers
from .models import GameData


class GameDataSerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField(read_only=True)

    class Meta:
        model = GameData
        fields = ["money", "height", "width", "level"]
