from django.db import models


# Create your models here.
class Monitoring(models.Model):
    day = models.DateField()
    count = models.IntegerField()
    list_users =models.ForeignKey('ListUsers', on_delete=models.PROTECT, default=1)

class ListUsers(models.Model):
    user = models.CharField(max_length=500)
