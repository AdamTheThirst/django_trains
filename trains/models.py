from django.db import models

from cities.models import City
# Create your models here.

class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, blank=False, null=False, default=False, verbose_name='Отправление', related_name='from_city_set')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, blank=False, null=False, default=False, verbose_name='Прибытие', related_name='to_city_set')

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']

    def __str__(self):
        return f'Поезд {self.name} из {self.from_city} в {self.to_city} идёт {self.travel_time} часов'
