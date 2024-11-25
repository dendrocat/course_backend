from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status

from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from app.mixins import DataMixin
from .models import GameData
from .serializers import GameDataSerializer


# Create your views here.
class GameView(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = "game/base.html"
    title = "Страница игры"

    sources = [
        {"name": "Локальные данные", "class": "local"},
        {"name": "Серверные данные", "class": "server"},
    ]
    fields = [
        {"name": "Уровень", "class": "level"},
        {"name": "Монеты", "class": "money"},
        {"name": "Высота", "class": "height"},
        {"name": "Ширина", "class": "width"},
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sources"] = self.sources
        context["fields"] = self.fields
        return context


class LeaderboardView(DataMixin, ListView):
    title = "Таблица лидеров"

    queryset = GameData.objects.select_related("user")
    context_object_name = "datas"
    template_name = "game/leaderboard.html"


class GameDataAPI(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # renderer_classes = [JSONRenderer]

    queryset = GameData.objects

    def get(self, request):
        data = self.queryset.get(user=request.user)

        serializer = GameDataSerializer(data)
        return Response(serializer.data)

    def patch(self, request):
        game_data = self.queryset.get(user=request.user)
        serializer = GameDataSerializer(game_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
