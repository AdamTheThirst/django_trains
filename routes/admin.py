from multiprocessing.reduction import register

from django.contrib import admin

from routes.models import Route


# Register your models here.

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    class Meta:
        model = Route
        ordering = ['from_city', 'route_travel_time']

    list_display = ('name',
                    'route_travel_time',
                    'from_city',
                    'to_city',)

    list_editable = ('route_travel_time',)

    list_filter = ('name',
                    'route_travel_time',
                    'from_city',
                    'to_city',)