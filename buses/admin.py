from django.contrib import admin

from buses.models import Bus


# Register your models here.

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    class Meta:
        model = Bus
        ordering = ['from_city', 'travel_time']

    list_display = ('name',
                    'travel_time',
                    'from_city',
                    'to_city',)

    list_editable = ('travel_time',)

    list_filter = ('name',
                    'travel_time',
                    'from_city',
                    'to_city',)


