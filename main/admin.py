from django.contrib import admin
from main.models import State, StateCapital, City
# Register your models here.


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbrev')


class CapitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'pop')


class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'zip_code')
    search_fields = ['city']


admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, CapitalAdmin)
admin.site.register(City, CityAdmin)
