from django.db import models
from user.models import User

class Todo(models.Model):
    _id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250)
    content = models.TextField()
    created_at = models.DateField()
    completed = models.BooleanField(default = False)
    owner = models.ForeignKey(User, related_name = 'todo', on_delete = models.CASCADE)