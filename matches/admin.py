from django.contrib import admin
from . import models

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display = ["id", "match_time", "match_status"]
    list_editable = ["match_status"]
    ordering = ['id']

class MatchRegAdmin(admin.ModelAdmin):
    list_display = ["playerid", "playername", "paid_through", "txnid"]
    ordering = ['id']


admin.site.register(models.Match, MatchAdmin)
admin.site.register(models.Match_1_Player, MatchRegAdmin)
admin.site.register(models.Match_2_Player, MatchRegAdmin)
admin.site.register(models.Match_3_Player, MatchRegAdmin)
admin.site.register(models.Match_4_Player, MatchRegAdmin)
admin.site.register(models.Match_5_Player, MatchRegAdmin)
admin.site.register(models.Match_6_Player, MatchRegAdmin)
