from django.db import models


class Station(models.Model):
    description = models.CharField(max_length = 255,null=True)
    power = models.IntegerField(blank=True,null=True)

    date_created = models.DateField(auto_now_add = True)
    detailed_time_created = models.TimeField(auto_now_add = True)
    

class Worker(models.Model):
    Name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255,null=True)
    

