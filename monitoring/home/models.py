from django.db import models


# Create your models here.
class Monitoring(models.Model):
    day = models.DateField()
    count = models.IntegerField()
