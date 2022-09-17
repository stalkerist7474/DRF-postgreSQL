from itertools import product
from tabnanny import verbose
from django.db import models



class Worker(models.Model):
    name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255,null=True)

    class Meta:
        
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name
    
class StoreProducts(models.Model):
    article_number = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)
    price = models.FloatField()
    unit_measurement_price = models.CharField(max_length = 30)
    quantity_in_store = models.IntegerField()


    class Meta:
        
        verbose_name = 'Наш товар'
        verbose_name_plural = 'Наши товары'

    def __str__(self):
        return self.name


class ProductParsed(models.Model):
    article_number = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)
    price = models.FloatField()
    unit_measurement_price = models.CharField(max_length = 30)

    class Meta:
        
        verbose_name = 'Спарсенный продукт'
        verbose_name_plural = 'Спарсенные продукты'

    def __str__(self):
        return self.name


class ParsValue(models.Model):
    Worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductParsed, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add = True)
    detailed_time_created = models.TimeField(auto_now_add = True)
    url_root = models.URLField()
    category = models.CharField(max_length = 255)

    class Meta:
        
        verbose_name = 'Парсинг лист'
        verbose_name_plural = 'Парсинг листы'

    def __str__(self):
        return self.id, self.date_created


