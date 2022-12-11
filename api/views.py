from django.shortcuts import render

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from api.models import Result, Player


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'username', 'password']


class Players(APIView):
    def post(self, request):
        player_data = request.data

        if "username" in player_data:
            if "password" in player_data:
                res = Player(username=player_data["username"], password=player_data["password"])
                res.save()
                return Response({"id": res.id, "username": res.username, "password": res.password,}, HTTP_201_CREATED)
            else:
                return Response({"msg": "Не указано поле password"}, HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Не указано поле username"}, HTTP_400_BAD_REQUEST)

    def get(self, request):
        players = []
        for player in Player.objects.all():
            players.append({
                "id": player.id,
                "username": player.username,
                "password": player.password
            })

        return Response(players, HTTP_200_OK)


class PlayerAuth(APIView):
    def get(self, request):
        player_data = request.data

        if "username" in player_data:
            if "password" in player_data:
                player_qs = Player.objects.filter(username=player_data["username"], password=player_data["password"])
                if player_qs.exists():
                    player = Player.objects.get(username=player_data["username"], password=player_data["password"])
                    return Response({"id": player.id}, HTTP_200_OK)
                else:
                    return Response({"msg": "Неверный username или пароль"}, HTTP_400_BAD_REQUEST)
            else:
                return Response({"msg": "Не указано поле password"}, HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Не указано поле username"}, HTTP_400_BAD_REQUEST)


class GameResults(APIView):
    def post(self, request):
        result = request.data
        player_qs = Player.objects.filter(id=result["id"])
        if player_qs.exists():
            player = Player.objects.get(id=result["id"])
            res = Result(player=player, score=result["score"])
            res.save()
            return Response({"msg": "Результат сохранён"}, HTTP_201_CREATED)
        else:
            return Response({"msg": "Игрока с таким id не существует"}, HTTP_400_BAD_REQUEST)

    def get(self, request):
        results = []
        for result in Result.objects.all():
            results.append({
                "id": result.player.id,
                "username": result.player.username,
                "score": result.score
            })

        return Response(results, HTTP_200_OK)



