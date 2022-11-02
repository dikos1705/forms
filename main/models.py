from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name=' Имя продукт', 
    blank=False, )
    description = models.TextField( verbose_name='Описание', )
    date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='фотография',)
    price = models.DecimalField(max_digits=10, verbose_name='Цена',decimal_places=2)
    is_available = models.BooleanField(default=True, verbose_name='Есть ли в наличии')
    class Meta:
        verbose_name ='Продукт'
        verbose_name_plural = 'Продукты'
    def __str__ (self):
        return self.name
