from django.db import models

class World(models.Model):
	"""each world contains multiple Riddles"""
	"""Worlds get more difficult"""
	num = models.IntegerField()

	
class Riddle(models.Model):
	"""represents a riddle, comprising a question and hints"""
	world = models.ForeignKey(World)
	question = models.TextField()
	num = models.IntegerField()

class Hint(models.Model):
	riddle = models.ForeignKey(Riddle)
	num = models.IntegerField()
	text = models.TextField()

class Answer(models.Model):
	riddle = models.ForeignKey(Riddle)
	value = models.CharField(max_length=200)

# Create your models here.
