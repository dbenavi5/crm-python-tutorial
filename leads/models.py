from django.db import models

# Created a database table names Lead and inside ther're 3 cols
class Lead(models.Model):
    first_name = models.CharField(max_length=20)   # string data type
    last_name = models.CharField(max_length=20)    # string data type
    age = models.IntegerField(default=0)           # integr data type