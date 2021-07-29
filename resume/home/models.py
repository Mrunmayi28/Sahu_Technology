from django.db import models
import datetime

# Create your models here.

class details(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Number = models.CharField(max_length=40)
    Dname = models.CharField(max_length=100)
    Branch = models.CharField(max_length=40)
    Dscore = models.CharField(max_length=40 , null= True)
    Styear = models.CharField(max_length=20 , null=True)
    Dyear = models.CharField(max_length=20)
    Hsc = models.CharField(max_length=50)
    Hscore = models.CharField(max_length=40 , null= True)
    Hyear = models.CharField(max_length=20)
    Ssc = models.CharField(max_length=50)
    Sscore = models.CharField(max_length=40)
    Syear = models.CharField(max_length=20)
    Experience = models.CharField(max_length=500)
    Skills = models.CharField(max_length=500)
    Awards = models.CharField(max_length=500)
    