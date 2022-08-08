from tabnanny import verbose
from django.db import models


class Station(models.Model):
    description = models.CharField(max_length = 255,null=True)
    power = models.IntegerField(blank=True,null=True)

    date_created = models.DateField(auto_now_add = True)
    detailed_time_created = models.TimeField(auto_now_add = True)

    class Meta:
        
        verbose_name = 'Подстанция'
        verbose_name_plural = 'Подстанции'

    def __str__(self):
        return self.description

    

class Worker(models.Model):
    name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255,null=True)

    class Meta:
        
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.Name
    

