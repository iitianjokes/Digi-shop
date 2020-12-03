from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length=100 , unique=True)
    password = models.CharField(max_length = 800)
    mobileno = models.CharField(max_length=10 , null=True , blank= True)