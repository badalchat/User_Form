from django.db import models
from datetime import *

# Create your models here.
class RegForm(models.Model):
    Name = models.CharField(max_length=50)
    DoB = models.DateField()
    Email = models.EmailField(max_length=60)
    Phone = models.CharField(max_length=14)
