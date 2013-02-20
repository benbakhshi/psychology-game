from django.db import models

class World(models.Model):
	"""each world contains multiple Level"""
	"""Worlds get more difficult"""
	num = models.IntegerField("World Number")
	
	def __unicode__(self):
		return unicode(self.num)
	
class Level(models.Model):
		
	world = models.ForeignKey(World)
	num = models.IntegerField("Level Number")
	points = models.IntegerField("Point Value")
	def __unicode__(self):
		return u"Level Number: %s" % (self.num)

class Hint(models.Model):
	
	level = models.ForeignKey(Level, related_name='hints')
	num = models.IntegerField()
	text = models.TextField()
	def __unicode__(self):
		return self.text

class Answer(models.Model):
	level = models.ForeignKey(Level, related_name='answers')
	value = models.CharField(max_length=200)

	def __unicode__(self):
		return self.value


#class Point(models.Model):
	
#	score = models.IntegerField("")
	

