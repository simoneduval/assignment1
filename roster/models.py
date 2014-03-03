#FILE: roster/models.py
from django.db import models
# Create your models here.

class Athlete(models.Model):
    name = models.CharField(unique=False, max_length=50)
    position = models.CharField(unique=False, max_length=12)
    year = models.CharField(unique=False, null=True, max_length=3)
    hometown = models.CharField(unique=False, max_length=50)
    highschool = models.CharField(unique=False, null=True, max_length=50)
    bio = models.CharField(max_length=400)
    imageurl = models.TextField(max_length =100)
    
    class Meta(object):
        ordering = ('position', 'name')
        
    def __unicode__(self):
        return U'%s %s' %(self.name, self.position)


class Best(models.Model):
    name = models.CharField(unique=False, max_length=50)
    position = models.CharField(unique=False, max_length=12)
    vault = models.CharField(unique=False, max_length=50)
    uneven_bars = models.CharField(unique=False, max_length=50)
    balance_beam = models.CharField(max_length=50)
    floor_exercise = models.CharField(max_length=200)
    all_around = models.CharField(max_length=50)
    imageurl = models.TextField(max_length =100)
    #athletes = models.ManyToManyField(Athlete)

    class Meta(object):
        verbose_name_plural = "Bests"
        ordering = ('vault','uneven_bars',)
        
    def __unicode__(self):
        return U'%s | %s' %(self.uneven_bars, self.vault)
    
class Personal(models.Model):
    major = models.CharField(unique=False, max_length=50)
    funny = models.CharField(unique=True, max_length=50)
    age = models.IntegerField(unique=False, null=True, max_length=50)
    met = models.CharField(unique=True, max_length=50)

    class Meta(object):
        ordering = ('major', 'funny')
        
    def __unicode__(self):
        return U'%s %s' %(self.funny, self.major)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Best, self).save(*args, **kwargs)
        

    

