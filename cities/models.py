from django.urls import reverse

from django.db import models

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return reverse('cities:cities_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['city']