from django.contrib import admin
from .models import Player, Result

admin.site.register(Player)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("player", "score")
