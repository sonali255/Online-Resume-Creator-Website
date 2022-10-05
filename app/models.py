from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,  primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.CharField(max_length=100)
    adress = models.TextField()
    clgname = models.CharField(max_length=100)
    clgyear = models.IntegerField()
    clgyear = models.CharField(max_length=100)
    clgcpi = models.CharField(max_length=100)
    cls12name = models.CharField(max_length=100)
    cls12year = models.IntegerField()
    cls12cpi = models.CharField(max_length=100)
    cls10name = models.CharField(max_length=100)
    cls10year = models.IntegerField()
    cls10cpi = models.CharField(max_length=100)
    intrest = models.CharField(max_length=100)
    planguages = models.CharField(max_length=100)
    toolsandtech = models.CharField(max_length=100)
    workexp = models.CharField(max_length=100, null=True, blank=True)
    projectname1 = models.CharField(max_length=100)
    projectdesc1 = models.TextField()
    projectname2= models.CharField(max_length=100, null=True, blank=True)
    projectdesc2 = models.TextField(null=True, blank=True)
    hobby1 = models.CharField(max_length=100)
    hobby2 = models.CharField(max_length=100)
    hobby3 = models.CharField(max_length=100)
    hobby4 = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname