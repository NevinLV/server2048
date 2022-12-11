from django.urls import path

from .views import GameResults, Players, PlayerAuth

urlpatterns = [
    path("results/", GameResults.as_view(), name="game_results"),
    path("player/", Players.as_view(), name="players"),
    path("player-auth/", PlayerAuth.as_view(), name="players"),
]
