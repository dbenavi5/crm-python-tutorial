from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Created a database table names Lead and inside ther're 3 cols
class Lead(models.Model):
    first_name = models.CharField(max_length=20)   # string data type
    last_name = models.CharField(max_length=20)    # string data type
    age = models.IntegerField(default=0)           # integer data type
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Agent(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email