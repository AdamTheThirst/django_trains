from django.contrib import admin

from trains.models import Train


# Register your models here.

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass