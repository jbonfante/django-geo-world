GeoDjango -- Starter Pack - V1
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
add world to your settings.py applications

Add Database Records from Shape Files
------------------------------------------
* All layers are imported by default
* If you want to change default layers loaded, change true/false in world/load.py

To initialize layer data launch:

python manage.py shell
<pre>
from world import load
load.run()
</pre>
