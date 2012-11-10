from django.contrib import admin
from dashboard.models import *

class TeamAdmin(admin.ModelAdmin):
	list_display = ('tid', 'name', 'location')

class SocialAdmin(admin.ModelAdmin):
	list_display = ('sid', 'tid', 'twitter')

class MembershipAdmin(admin.ModelAdmin):
	list_display = ('mid', 'tid', 'uid', 'admin',)

class GameAdmin(admin.ModelAdmin):
	list_display = ('gid', 'tid', 'done', 'score', 'date',)

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('pid', 'gid', 'uid', 'position', 'attending')

admin.site.register(Team, TeamAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
