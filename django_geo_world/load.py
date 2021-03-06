from adaptor.model import CsvDbModel
from django.utils.log import getLogger

__author__ = 'jbonfante'

import os
from django.contrib.gis.utils import LayerMapping
from django_geo_world.models import *

logger = getLogger(__name__)


# List of shape files that are loaded from data directories

city_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cities.shp'))
uscity_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cities_dtl.shp'))
state_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/dtl_st.shp'))
world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS-0.3.shp'))
zip_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/zip_poly.shp'))
urban_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/urban.shp'))
county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/dtl_cnty.shp'))
placepoint_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/places.shp'))
zipcode_data = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/zip_code_database.csv'))

# Helper shape data definition to streamline loading process
class ShapeDataDefinition(object):
    shape_file = None
    mapping = None
    model = None
    transform = None
    encoding= None
    def __init__(self, shape_file, mapping, model, transform=False, encoding='iso-8859-1'):
        self.shape_file = shape_file
        self.mapping = mapping
        self.model = model
        self.transform = transform
        self.encoding = encoding



# Initial loading variables for filling up the borders database tables
# If you don't want to load the entire dataset:
# Comment out the lines you do not with the load process to consider
load_init = {}
load_init["world_city"] = ShapeDataDefinition(shape_file=city_shp, model=CityBorder, mapping=cityborder_mapping)
load_init["state"] = ShapeDataDefinition(shape_file=state_shp, model=StateBorder, mapping=stateborder_mapping)
load_init["us_city"] = ShapeDataDefinition(shape_file=uscity_shp, model=USCityBorder, mapping=uscityborder_mapping)
load_init["world"] = ShapeDataDefinition(shape_file=world_shp, model=WorldBorder, mapping=worldborder_mapping)
load_init["zip"] = ShapeDataDefinition(shape_file=zip_shp,model=ZipcodeBorder, mapping=zipcodeborder_mapping)
load_init["urban"] = ShapeDataDefinition(shape_file=urban_shp, model=UrbanBorder, mapping=urbanborder_mapping)
load_init["county"] = ShapeDataDefinition(shape_file=county_shp, model=CountyBorder, mapping=countyborder_mapping)
load_init["places"] = ShapeDataDefinition(shape_file=placepoint_shp, model=PlacePoint, mapping=placepoint_mapping)


class ZipcodeCSVModel(CsvDbModel):

    class Meta:
        dbModel = Zipcode
        delimiter = ','
        exclude = ['id']


def fix_area_codes():
    print('Stripping Blank Spaces from area codes')
    saved = Zipcode.objects.all()
    for code in saved:
        code.area_codes = code.area_codes.strip(' ')
        code.save()
    print('Done Stripping')


def load_zipcode(csvfile=zipcode_data):
    print('Loading Zipcode information')
    zip_code_list = ZipcodeCSVModel.import_data(data=open(csvfile))
    results = 'Loaded Zipcode data, total: {}'.format(len(zip_code_list))
    print(results)
    fix_area_codes()
    print('Done')

def auto_load():
    data = os.path.abspath(os.path.join(os.path.dirname('.'), 'django_geo_world/data/zip_code_database.csv'))
    load_zipcode(data)





def run(verbose=True, options=load_init):
    """
    Run command to launch mapping of shape files to database models
    :param verbose:
    :param options:
    :return:
    """
    for item in options:
        target = options[item]
        lm = LayerMapping(target.model, target.shape_file, target.mapping,
                          transform=target.transform, encoding=target.encoding)

        lm.save(strict=False, verbose=verbose)
    load_zipcode()



# def class_for_name(module_name, class_name):
#     # load the module, will raise ImportError if module cannot be loaded
#     m = importlib.import_module(module_name)
#     # get the class, will raise AttributeError if class cannot be found
#     c = getattr(m, class_name)
#     return c


