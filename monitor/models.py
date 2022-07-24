from django.db import models


class StatisticUsers(models.Model):
    day = models.DateField()
    count = models.IntegerField()
    list_users =models.ForeignKey('ListUsers', on_delete=models.PROTECT)

class ListUsers(models.Model):
    user = models.CharField(max_length=500)
