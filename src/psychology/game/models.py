from django.db import models

class Riddle(models.Model):
	"""represents a riddle, comprising a question and hints"""
	question = models.TextField()


class Hint(models.Model):
	riddle = models.ForeignKey(Riddle)
	num = models.IntegerField()
	text = models.TextField()

class Answer(models.Model):
	riddle = models.ForeignKey(Riddle)
	value = models.CharField(max_length=200)

# Create your models here.
