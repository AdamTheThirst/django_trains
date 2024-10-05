from django.apps import AppConfig


class BusesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buses'
    verbose_name = 'Автобус'
    verbose_name_plural = 'Автобусы'