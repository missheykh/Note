from typing import Text
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UsersNote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    title=models.CharField(max_length=40)
    text=models.TextField()
    shared_users=models.ManyToManyField(User,related_name='shared',blank=True)

    def __str__(self):
        return f"{self.user}:{self.title}"



        
