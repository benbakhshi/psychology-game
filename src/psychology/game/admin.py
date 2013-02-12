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
	(None, 		{'fields': ['question']})
	]
	inlines = [HintInline, AnswerInline]
	list_display = ('question',)


admin.site.register(models.Riddle, RiddleAdmin)

