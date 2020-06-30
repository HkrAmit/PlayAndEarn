from django.contrib import admin
from .models import players, temp_player

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["pubg_id", "pubg_name","mobile", "email"]
    ordering = ['pubg_id']

class TempPlayerAdmin(admin.ModelAdmin):
    list_display = ["pubg_id", "pubg_name","mobile", "otp", "otp2", "otp3", "exp_time"]
    ordering = ['pubg_id']


admin.site.register(players, PlayerAdmin)
admin.site.register(temp_player, TempPlayerAdmin)