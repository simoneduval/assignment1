#FILE: roster/models.py
from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(unique=True, max_length=50)
