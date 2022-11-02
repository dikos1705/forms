from django.db import models

# Create your models here.

class Car(models.Model):
    mark = models.CharField(max_length=255,verbose_name='Марка')
    model = models.CharField(max_length=255,verbose_name='Модель')
    description = models.TextField(blank=True,verbose_name='Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name='фотография')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='время создания')
    time_upgrade = models.DateTimeField(auto_now=True,verbose_name='время изменения')
    price = models.CharField(max_length=255,verbose_name='цена')
    is_published = models.BooleanField(default=True,verbose_name='Публиковано_ли')
    def __str__(self):
        return self.mark+" "+self.model
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = [ 'time_create', 'mark']
