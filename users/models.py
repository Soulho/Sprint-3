from django.db import models

# Create your models here.
class Client(models.Model):
     id = models.AutoField(primary_key=True)
     login = models.CharField(max_length=200)
     password = models.CharField(max_length=200)
     isConfirmed = models.BooleanField(default=False)
     
     def __str__(self):
        return self.name
