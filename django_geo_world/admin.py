__author__ = 'jbonfante'
from django.contrib.gis import admin
from .models import *

class WorldBorderAdmin(admin.GeoModelAdmin):
    list_display =  ('name' , 'pop2005', 'un','region','subregion', 'lat', 'lon',)
    list_display_links = ('name', 'pop2005','un','region', 'subregion','lat','lon',)
    search_fields = ['name']

class CityBorderAdmin(admin.GeoModelAdmin):
    list_display = ('name','country','population', 'capital')
    list_filter = ['country']
    search_fields = ['name','country']

class StateBorderAdmin(admin.GeoModelAdmin):
    list_display = ('state_name','state_abbr',)

    search_fields = ['state_name',]

class ZipcodeBorderAdmin(admin.GeoModelAdmin):
    list_display = ('zip','state','po_name','pop2007')

    search_fields = ['zip','state',]

class USCityBorderAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'st_abbrev', 'status')

    search_fields = ['name','st_abbrev']
class CountyBorderAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'state_name', 'cnty_fips')

    search_fields = ['name','state_name']
class UrbanBorderAdmin(admin.GeoModelAdmin):
    list_display = ('name','lsad_desc', 'households', 'hse_units')

    search_fields = ['name','households','lsad_desc']
    list_filter = ['lsad_desc']


class PlacePointAdmin(admin.GeoModelAdmin):
    list_display = ('name','st', 'pop2000','houseunits')

    search_fields = ['name','st','pop2000','houseunits']
    list_filter = ['place_class']


admin.site.register(WorldBorder, WorldBorderAdmin)
admin.site.register(CityBorder, CityBorderAdmin)
admin.site.register(StateBorder, StateBorderAdmin)
admin.site.register(ZipcodeBorder, ZipcodeBorderAdmin)
admin.site.register(USCityBorder, USCityBorderAdmin)
admin.site.register(CountyBorder, CountyBorderAdmin)
admin.site.register(PlacePoint, PlacePointAdmin)
admin.site.register(UrbanBorder, UrbanBorderAdmin)