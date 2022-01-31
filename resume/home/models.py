from django.db import models

# Create your models here.
class modelaccept(models.Model):
    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    specification = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=40, null=True)
    link = models.CharField(max_length=100 , null=True)
    dname = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=40 , null=True)
    dscore = models.CharField(max_length=40 , null= True)
    styear = models.CharField(max_length=20 , null=True)
    dyear = models.CharField(max_length=20, null=True)
    hsc = models.CharField(max_length=50, null=True)
    hscore = models.CharField(max_length=40 , null= True)
    hyear = models.CharField(max_length=20, null=True)
    ssc = models.CharField(max_length=50, null=True)
    sscore = models.CharField(max_length=40, null=True)
    syear = models.CharField(max_length=20, null=True)
    experience = models.TextField(max_length=500, null=True)
    skills = models.TextField(max_length=500, null=True)
    awards = models.TextField(max_length=500, null = True)