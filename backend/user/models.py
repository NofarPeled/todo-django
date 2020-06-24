from django.db import models

class User(models.Model):
    _id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 100, unique = True)
    email = models.EmailField(max_length = 100, unique = True)
    password = models.CharField(max_length = 50)