from django.db import models
from django.utils import timezone
from getRank import getRank

class Day(models.Model) :
    date = models.DateTimeField(default=timezone.now)
    rank= models.IntegerField(default=9999)
    solved = models.IntegerField(default = 0)

class Person(models.Model) :
    personId = models.CharField(max_length=20)
    personPassword = models.CharField(max_length=20)