Django-Geo-World -- Starter Pack - V1.2
========================================
*View the [source of this content](https://github.com/jbonfante/django-geo-world)*
*author's [blog](http://blog.juanbonfante.com)*


What it Does
------------------------------------------
This app gives you a fairly thorough database to do most geocoding right in Django.

If you have a point, or lat/long you can use one/or multiple model(s) to extract
data from that point, zipcode, county, country, state, etc.

The layers are composed of multiple open sources, and you can add models as needed.
*Addition Layer [sources](http://www.baruch.cuny.edu/geoportal/data/esri/esri_usa.htm)*

Install
------------------------------------------

*add django_geo_world to your INSTALLED_APPS settings.py
*run syncdb to create db tables

Add Database Records from Shape Files
------------------------------------------
* All layers are imported by default
* If you want to change default layers loaded, change true/false in world/load.py

To initialize layer data launch:

python manage.py shell
<pre>
from django_geo_world.world import load
load.run()
</pre>

Running Sample App
---------------------------------------------
Sample app uses PostGre + PostGIS database.

Make sure to enable GIS extensions on your database, more information on how to setup Django + PostGIS
* Django Docs [sources](https://docs.djangoproject.com/en/1.6/ref/contrib/gis/install/postgis/#post-installation)

TODO
---------------------------------------------
* Add more shapefiles to list
** Streets
** Places
** Other Census Data
* Create helper methods to search through all models and return information gathered from all
* Further Documentation
* Add Unit Tests
