from django.contrib import admin
from football.models import Team, League, Match, Result

admin.site.register(Team)
admin.site.register(League)
admin.site.register(Match)
admin.site.register(Result)
