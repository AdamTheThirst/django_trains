from django.db import models

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.city

    class Meta:
        verbos_name = 'Город'
        verbos_name_plural = 'Города'
        ordering = ['city']