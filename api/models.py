from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Имя игрока', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.username


class Result(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField('Счёт')

    def __str__(self):
        return f'{self.player.username} (id: {self.player.id}): {self.score}'
