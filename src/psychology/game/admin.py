from django.contrib import admin
from psychology.game import models

class HintInline(admin.TabularInline):
	model = models.Hint
	extra = 1

class AnswerInline(admin.TabularInline):
	model = models.Answer
	extra = 2
	list_display = ('answer',)

class RiddleAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, 		{'fields': ['question']}),
	
	]
	inlines = [HintInline, AnswerInline]
	
	list_display = ('question', 'get_world')
	
	def get_world(self, obj):
		return obj.world.num
	get_world.short_description = 'World'

class RiddleInline(admin.TabularInline):
	model = models.Riddle
	extra = 2
	
class WorldAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, 		{'fields': ['num']})
	]
	
	def get_riddle(self, obj):
		return obj.riddle_set.count()
	
	get_riddle.short_description = 'Question'
	
	inlines = [RiddleInline,]
	list_display = ('num', 'get_riddle')

admin.site.register(models.World, WorldAdmin)
admin.site.register(models.Riddle, RiddleAdmin)

