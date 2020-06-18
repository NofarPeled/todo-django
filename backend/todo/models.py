from django.db import models

class Todo(models.Model):
    _id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250)
    content = models.TextField()
    created_at = models.DateField()
    complete = models.BooleanField(default = False)