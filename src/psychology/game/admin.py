from django.contrib import admin
from psychology.game import models

class HintInline(admin.TabularInline):
	model = models.Hint
	extra = 1

class AnswerInline(admin.TabularInline):
	model = models.Answer
	extra = 2
	list_display = ('answer',)

class LevelAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, 		{'fields': ['question']}),
	
	]
	inlines = [HintInline, AnswerInline]
	
	list_display = ('question', 'get_world')
	
	def get_world(self, obj):
		return obj.world.num
	get_world.short_description = 'World'

class LevelInline(admin.TabularInline):
	model = models.Level
	extra = 2
	
class WorldAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, 		{'fields': ['num']})
	]
	
	def get_level(self, obj):
		return obj.level_set.count()
	
	get_level.short_description = 'Question'
	
	inlines = [LevelInline,]
	list_display = ('num', 'get_level')

admin.site.register(models.World, WorldAdmin)
admin.site.register(models.Level, LevelAdmin)

