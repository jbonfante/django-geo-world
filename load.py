__author__ = 'jbonfante'

import os
from django.contrib.gis.utils import LayerMapping
from models import *

__world_city = True
__us_city = True
__state = True
__world = True
__zip = True
__urban = True
__county = False



city_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cities.shp'))
uscity_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cities_dtl.shp'))
state_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/dtl_st.shp'))
world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS-0.3.shp'))
zip_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/zip_poly.shp'))
urban_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/urban.shp'))
county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/dtl_cnty.shp'))


def run(verbose=True, world_city = __world_city, us_city = __us_city, state = __state, world = __world, zipcode = __zip, urban = __urban, county = __county):
    if world:
        lm = LayerMapping(WorldBorder, world_shp, worldborder_mapping,
                          transform=False, encoding='iso-8859-1')

        lm.save(strict=False, verbose=verbose)
    if state:
        lm = LayerMapping(StateBorder, state_shp, stateborder_mapping,
                          transform=False, encoding='iso-8859-1')

        lm.save(strict=False, verbose=verbose)
    if county:
        lm = LayerMapping(CountyBorder, county_shp, countyborder_mapping,
                          transform=False, encoding='iso-8859-1')

        lm.save(strict=False, verbose=verbose)

    if world_city:
        lm = LayerMapping(CityBorder, city_shp, cityborder_mapping,
                          transform=False, encoding='iso-8859-1')

        lm.save(strict=False, verbose=verbose)
    if zipcode:
        lm = LayerMapping(ZipcodeBorder, zip_shp, zipcodeborder_mapping,
                          transform=False, encoding='iso-8859-1')

        lm.save(strict=False, verbose=verbose)
    if us_city:
        lm = LayerMapping(USCityBorder, uscity_shp, uscityborder_mapping,
                          transform=False, encoding='iso-8859-1')

        lm.save(strict=False, verbose=verbose)

