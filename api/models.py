from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=250)
    bdate = models.DateField()
    address = models.CharField(max_length=250)
    zipcode = models.IntegerField()
    
    def __str__(self):
        return self.name
    