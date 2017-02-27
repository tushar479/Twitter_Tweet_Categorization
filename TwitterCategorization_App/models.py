from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class UserDetails(models.Model):
	username = models.TextField(max_length=500)
	def __str__ (self):
		return self.username


class TrainedDataSet(models.Model):
	Tweets = models.TextField(max_length=500)
	Type = models.CharField(max_length=50)
	def __unicode__(self):
		return u"%s, %s" % (self.Tweets, self.Type) 

class TestDataSet(models.Model):
	Tweets = models.TextField(max_length=500)
	Type = models.CharField(max_length=50,blank=True, null=True)
	def __unicode__(self):
		return u"%s, %s" % (self.Tweets, self.Type) 
