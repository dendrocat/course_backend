from django.urls import path
from .views import GameView, GameDataAPI, LeaderboardView

app_name = "game"

urlpatterns = [
    path("", GameView.as_view(), name="index"),
    path("api", GameDataAPI.as_view(), name="api"),
    path("leaders", LeaderboardView.as_view(), name="leaderboard"),
]
