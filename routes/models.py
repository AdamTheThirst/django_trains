from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City
from buses.models import Bus
# Create your models here.

class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Маршрут')
    rout_travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути (маршрут)')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, blank=False, null=False, default=False, verbose_name='Отправление', related_name='route_from_city_set')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, blank=False, null=False, default=False, verbose_name='Прибытие', related_name='route_to_city_set')
    buses = models.ManyToManyField(Bus, verbose_name='Список автобусов')

    # def clean(self):
    #     if self.from_city == self.to_city:
    #         raise ValidationError('Города прибытия и отправления должны быть разными')
    #     qs = self.__class__.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(id=self.id)
    #     if qs.exists():
    #         raise ValidationError('Такой мартшрут уже есть')
    #
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'Маршрут {self.name} из {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_time']
