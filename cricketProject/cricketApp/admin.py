from django.contrib import admin
from cricketApp.models import Team,Player,Match

# Register your models here.


class Admin_Team(admin.ModelAdmin):
    list_display = ['name','logo_uri','club_state']
    readonly_fields = ['matches_played','matches_won','matches_lost','team_points']

class Admin_Player(admin.ModelAdmin):
    list_display = ['first_name','last_name','profile_picture','jersey_number','country','team',
                    'no_of_matches','runs','highest_score','fifties','hundreds','strike_rate']

class Admin_Match(admin.ModelAdmin):
    list_display = ['match_date','location','team1','team2','team1_score','team2_score','match_winner']


admin.site.register(Team,Admin_Team)
admin.site.register(Player,Admin_Player)
admin.site.register(Match,Admin_Match)

