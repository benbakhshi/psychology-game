from django.db import models

class World(models.Model):
	"""each world contains multiple Level"""
	"""Worlds get more difficult"""
	num = models.IntegerField()

	
class Level(models.Model):
	"""represents a level, comprising a question and hints"""
	world = models.ForeignKey(World)
	question = models.TextField()
	num = models.IntegerField()

class Hint(models.Model):
	level = models.ForeignKey(Level)
	num = models.IntegerField()
	text = models.TextField()

class Answer(models.Model):
	level = models.ForeignKey(Level)
	value = models.CharField(max_length=200)

# Create your models here.
