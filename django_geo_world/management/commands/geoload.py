# from __future__ import absolute_import, unicode_literals
#
# from django.contrib.gis.utils import LayerMapping
# from django_geo_world.models import *
#
# import importlib
# import os
# import sys
#
# from django.core.management.base import NoArgsCommand
# from ._load import ShapeDataDefinition
#
# __author__ = 'juanrbonfante'
# city_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/cities.shp'))
# uscity_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/cities_dtl.shp'))
# state_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/dtl_st.shp'))
# world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/TM_WORLD_BORDERS-0.3.shp'))
# zip_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/zip_poly.shp'))
# urban_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/urban.shp'))
# county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/dtl_cnty.shp'))
# placepoint_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/places.shp'))
#
#
# def GeoWorldCommand(NoArgsCommand):
#     """
#     Preload Database with provided geo libraries
#     :param BaseCommand:
#     """
#     help = 'GeoWorld Command for Django to Preload data'
#     args = 'None for now.'
#     # Initial loading variables for filling up the borders database tables
#     # If you don't want to load the entire dataset:
#     # Comment out the lines you do not with the load process to consider
#     load_init = {}
#
#     def __init__(self):
#         super(GeoWorldCommand, self).__init__(self)
#         # city_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/cities.shp'))
#         #
#         # uscity_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/cities_dtl.shp'))
#         # state_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/dtl_st.shp'))
#         # world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/TM_WORLD_BORDERS-0.3.shp'))
#         # zip_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/zip_poly.shp'))
#         # urban_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/urban.shp'))
#         # county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/dtl_cnty.shp'))
#         # placepoint_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
#         #                                               '../data/places.shp'))  # Initial loading variables for filling up
#         # the borders database tables
#         # If you don't want to load the entire dataset:
#         # Comment out the lines you do not with the load process to consider
#         self.load_init["world_city"] = ShapeDataDefinition(shape_file=city_shp, model=CityBorder,
#                                                            mapping=cityborder_mapping)
#         self.load_init["state"] = ShapeDataDefinition(shape_file=state_shp, model=StateBorder,
#                                                       mapping=stateborder_mapping)
#         self.load_init["us_city"] = ShapeDataDefinition(shape_file=uscity_shp, model=USCityBorder,
#                                                         mapping=uscityborder_mapping)
#         self.load_init["world"] = ShapeDataDefinition(shape_file=world_shp, model=WorldBorder,
#                                                       mapping=worldborder_mapping)
#         self.load_init["zip"] = ShapeDataDefinition(shape_file=zip_shp, model=ZipcodeBorder,
#                                                     mapping=zipcodeborder_mapping)
#         self.load_init["urban"] = ShapeDataDefinition(shape_file=urban_shp, model=UrbanBorder,
#                                                       mapping=urbanborder_mapping)
#         self.load_init["county"] = ShapeDataDefinition(shape_file=county_shp,
#                                                        model=CountyBorder,
#                                                        mapping=countyborder_mapping)
#         self.load_init["places"] = ShapeDataDefinition(shape_file=placepoint_shp,
#                                                        model=PlacePoint,
#                                                        mapping=placepoint_mapping)
#
#
#     def handle_noargs(self, **options):
#         options = i
#         for item in options:
#             target = options[item]
#             lm = LayerMapping(target.model, target.shape_file, target.mapping,
#                               transform=target.transform, encoding=target.encoding)
#
#             lm.save(strict=False, verbose=verbose)
