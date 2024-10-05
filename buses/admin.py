from django.contrib import admin

from buses.models import Bus


# Register your models here.

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    pass