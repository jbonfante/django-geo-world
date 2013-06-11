from django.contrib.gis.db import models

# Create your models here.
class WorldBorder(models.Model):
    class Meta:
        ordering = ['name']
        index_together = [['lat','lon']]
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()



    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name
    # Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborder_mapping = {
        'fips' : 'FIPS',
        'iso2' : 'ISO2',
        'iso3' : 'ISO3',
        'un' : 'UN',
        'name' : 'NAME',
        'area' : 'AREA',
        'pop2005' : 'POP2005',
        'region' : 'REGION',
        'subregion' : 'SUBREGION',
        'lon' : 'LON',
        'lat' : 'LAT',
        'geom' : 'MULTIPOLYGON',
        }

class StateBorder(models.Model):
    class Meta:
        ordering = ['state_name']

    state_name = models.CharField(max_length=50)
    state_fips = models.CharField(max_length=2)
    sub_region = models.CharField(max_length=20)
    state_abbr = models.CharField(max_length=2)
    pop2000 = models.IntegerField()
    pop2007 = models.IntegerField()
    pop00_sqmi = models.FloatField()
    pop07_sqmi = models.FloatField()
    white = models.IntegerField()
    black = models.IntegerField()
    ameri_es = models.IntegerField()
    asian = models.IntegerField()
    hawn_pi = models.IntegerField()
    other = models.IntegerField()
    mult_race = models.IntegerField()
    hispanic = models.IntegerField()
    males = models.IntegerField()
    females = models.IntegerField()
    age_under5 = models.IntegerField()
    age_5_17 = models.IntegerField()
    age_18_21 = models.IntegerField()
    age_22_29 = models.IntegerField()
    age_30_39 = models.IntegerField()
    age_40_49 = models.IntegerField()
    age_50_64 = models.IntegerField()
    age_65_up = models.IntegerField()
    med_age = models.FloatField()
    med_age_m = models.FloatField()
    med_age_f = models.FloatField()
    households = models.IntegerField()
    ave_hh_sz = models.FloatField()
    hsehld_1_m = models.IntegerField()
    hsehld_1_f = models.IntegerField()
    marhh_chd = models.IntegerField()
    marhh_no_c = models.IntegerField()
    mhh_child = models.IntegerField()
    fhh_child = models.IntegerField()
    families = models.IntegerField()
    ave_fam_sz = models.FloatField()
    hse_units = models.IntegerField()
    vacant = models.IntegerField()
    owner_occ = models.IntegerField()
    renter_occ = models.IntegerField()
    no_farms97 = models.FloatField()
    avg_size97 = models.FloatField()
    crop_acr97 = models.FloatField()
    avg_sale97 = models.FloatField()
    sqmi = models.IntegerField()
    oid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.state_name


# Auto-generated `LayerMapping` dictionary for StateBorder model
stateborder_mapping = {
    'state_name' : 'STATE_NAME',
    'state_fips' : 'STATE_FIPS',
    'sub_region' : 'SUB_REGION',
    'state_abbr' : 'STATE_ABBR',
    'pop2000' : 'POP2000',
    'pop2007' : 'POP2007',
    'pop00_sqmi' : 'POP00_SQMI',
    'pop07_sqmi' : 'POP07_SQMI',
    'white' : 'WHITE',
    'black' : 'BLACK',
    'ameri_es' : 'AMERI_ES',
    'asian' : 'ASIAN',
    'hawn_pi' : 'HAWN_PI',
    'other' : 'OTHER',
    'mult_race' : 'MULT_RACE',
    'hispanic' : 'HISPANIC',
    'males' : 'MALES',
    'females' : 'FEMALES',
    'age_under5' : 'AGE_UNDER5',
    'age_5_17' : 'AGE_5_17',
    'age_18_21' : 'AGE_18_21',
    'age_22_29' : 'AGE_22_29',
    'age_30_39' : 'AGE_30_39',
    'age_40_49' : 'AGE_40_49',
    'age_50_64' : 'AGE_50_64',
    'age_65_up' : 'AGE_65_UP',
    'med_age' : 'MED_AGE',
    'med_age_m' : 'MED_AGE_M',
    'med_age_f' : 'MED_AGE_F',
    'households' : 'HOUSEHOLDS',
    'ave_hh_sz' : 'AVE_HH_SZ',
    'hsehld_1_m' : 'HSEHLD_1_M',
    'hsehld_1_f' : 'HSEHLD_1_F',
    'marhh_chd' : 'MARHH_CHD',
    'marhh_no_c' : 'MARHH_NO_C',
    'mhh_child' : 'MHH_CHILD',
    'fhh_child' : 'FHH_CHILD',
    'families' : 'FAMILIES',
    'ave_fam_sz' : 'AVE_FAM_SZ',
    'hse_units' : 'HSE_UNITS',
    'vacant' : 'VACANT',
    'owner_occ' : 'OWNER_OCC',
    'renter_occ' : 'RENTER_OCC',
    'no_farms97' : 'NO_FARMS97',
    'avg_size97' : 'AVG_SIZE97',
    'crop_acr97' : 'CROP_ACR97',
    'avg_sale97' : 'AVG_SALE97',
    'sqmi' : 'SQMI',
    'oid' : 'OID',
    'geom' : 'MULTIPOLYGON',
    }



class CityBorder(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=12)
    population = models.FloatField()
    capital = models.CharField(max_length=1)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()


    class Meta:
        ordering = ['name', 'country']
        index_together = [['name', 'country'], ]


    def __unicode__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for CityBorder model
cityborder_mapping = {
    'name' : 'NAME',
    'country' : 'COUNTRY',
    'population' : 'POPULATION',
    'capital' : 'CAPITAL',
    'geom' : 'MULTIPOINT',
    }

class ZipcodeBorder(models.Model):
    zip = models.CharField(max_length=5)
    po_name = models.CharField(max_length=28, verbose_name='City')
    state = models.CharField(max_length=2)
    sumblkpop = models.IntegerField()
    pop2007 = models.IntegerField()
    pop07_sqmi = models.FloatField()
    sqmi = models.FloatField()
    oid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        ordering = ['zip',]
        index_together = [['zip', 'state'], ]

    def __unicode__(self):
        return self.zip

# Auto-generated `LayerMapping` dictionary for ZipcodeBorder model
zipcodeborder_mapping = {
    'zip' : 'ZIP',
    'po_name' : 'PO_NAME',
    'state' : 'STATE',
    'sumblkpop' : 'SUMBLKPOP',
    'pop2007' : 'POP2007',
    'pop07_sqmi' : 'POP07_SQMI',
    'sqmi' : 'SQMI',
    'oid' : 'OID',
    'geom' : 'MULTIPOLYGON',
    }

class USCityBorder(models.Model):
    feature = models.CharField(max_length=21)
    name = models.CharField(max_length=48)
    st_abbrev = models.CharField(max_length=2)
    fips = models.CharField(max_length=5)
    place_fips = models.CharField(max_length=5)
    pop_2000 = models.IntegerField()
    pop2007 = models.IntegerField()
    status = models.CharField(max_length=30)
    oid = models.IntegerField()
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['st_abbrev','name',]

# Auto-generated `LayerMapping` dictionary for USCityBorder model
uscityborder_mapping = {
    'feature' : 'FEATURE',
    'name' : 'NAME',
    'st_abbrev' : 'ST_ABBREV',
    'fips' : 'FIPS',
    'place_fips' : 'PLACE_FIPS',
    'pop_2000' : 'POP_2000',
    'pop2007' : 'POP2007',
    'status' : 'STATUS',
    'oid' : 'OID',
    'geom' : 'MULTIPOINT',
    }

class UrbanBorder(models.Model):
    ua_id = models.CharField(max_length=5)
    name = models.CharField(max_length=40)
    lsad = models.CharField(max_length=2)
    lsad_desc = models.CharField(max_length=14)
    pop2000 = models.IntegerField()
    pop00_sqmi = models.FloatField()
    households = models.IntegerField()
    hse_units = models.IntegerField()
    sqmi = models.FloatField()
    oid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for UrbanBorder model
urbanborder_mapping = {
    'ua_id' : 'UA_ID',
    'name' : 'NAME',
    'lsad' : 'LSAD',
    'lsad_desc' : 'LSAD_DESC',
    'pop2000' : 'POP2000',
    'pop00_sqmi' : 'POP00_SQMI',
    'households' : 'HOUSEHOLDS',
    'hse_units' : 'HSE_UNITS',
    'sqmi' : 'SQMI',
    'oid' : 'OID',
    'geom' : 'MULTIPOLYGON',
    }

class CountyBorder(models.Model):
    name = models.CharField(max_length=32)
    state_name = models.CharField(max_length=25)
    state_fips = models.CharField(max_length=2)
    cnty_fips = models.CharField(max_length=3)
    fips = models.CharField(max_length=5)
    pop2000 = models.IntegerField()
    pop2007 = models.IntegerField()
    pop00_sqmi = models.FloatField()
    pop07_sqmi = models.FloatField()
    white = models.IntegerField()
    black = models.IntegerField()
    ameri_es = models.IntegerField()
    asian = models.IntegerField()
    hawn_pi = models.IntegerField()
    other = models.IntegerField()
    mult_race = models.IntegerField()
    hispanic = models.IntegerField()
    males = models.IntegerField()
    females = models.IntegerField()
    age_under5 = models.IntegerField()
    age_5_17 = models.IntegerField()
    age_18_21 = models.IntegerField()
    age_22_29 = models.IntegerField()
    age_30_39 = models.IntegerField()
    age_40_49 = models.IntegerField()
    age_50_64 = models.IntegerField()
    age_65_up = models.IntegerField()
    med_age = models.FloatField()
    med_age_m = models.FloatField()
    med_age_f = models.FloatField()
    households = models.IntegerField()
    ave_hh_sz = models.FloatField()
    hsehld_1_m = models.IntegerField()
    hsehld_1_f = models.IntegerField()
    marhh_chd = models.IntegerField()
    marhh_no_c = models.IntegerField()
    mhh_child = models.IntegerField()
    fhh_child = models.IntegerField()
    families = models.IntegerField()
    ave_fam_sz = models.FloatField()
    hse_units = models.IntegerField()
    vacant = models.IntegerField()
    owner_occ = models.IntegerField()
    renter_occ = models.IntegerField()
    no_farms97 = models.FloatField()
    avg_size97 = models.FloatField()
    crop_acr97 = models.FloatField()
    avg_sale97 = models.FloatField()
    sqmi = models.FloatField()
    oid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        ordering = ['state_name','name',]
        index_together = [['state_name', 'name'], ]

    def __unicode__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for CountyBorder model
countyborder_mapping = {
    'name' : 'NAME',
    'state_name' : 'STATE_NAME',
    'state_fips' : 'STATE_FIPS',
    'cnty_fips' : 'CNTY_FIPS',
    'fips' : 'FIPS',
    'pop2000' : 'POP2000',
    'pop2007' : 'POP2007',
    'pop00_sqmi' : 'POP00_SQMI',
    'pop07_sqmi' : 'POP07_SQMI',
    'white' : 'WHITE',
    'black' : 'BLACK',
    'ameri_es' : 'AMERI_ES',
    'asian' : 'ASIAN',
    'hawn_pi' : 'HAWN_PI',
    'other' : 'OTHER',
    'mult_race' : 'MULT_RACE',
    'hispanic' : 'HISPANIC',
    'males' : 'MALES',
    'females' : 'FEMALES',
    'age_under5' : 'AGE_UNDER5',
    'age_5_17' : 'AGE_5_17',
    'age_18_21' : 'AGE_18_21',
    'age_22_29' : 'AGE_22_29',
    'age_30_39' : 'AGE_30_39',
    'age_40_49' : 'AGE_40_49',
    'age_50_64' : 'AGE_50_64',
    'age_65_up' : 'AGE_65_UP',
    'med_age' : 'MED_AGE',
    'med_age_m' : 'MED_AGE_M',
    'med_age_f' : 'MED_AGE_F',
    'households' : 'HOUSEHOLDS',
    'ave_hh_sz' : 'AVE_HH_SZ',
    'hsehld_1_m' : 'HSEHLD_1_M',
    'hsehld_1_f' : 'HSEHLD_1_F',
    'marhh_chd' : 'MARHH_CHD',
    'marhh_no_c' : 'MARHH_NO_C',
    'mhh_child' : 'MHH_CHILD',
    'fhh_child' : 'FHH_CHILD',
    'families' : 'FAMILIES',
    'ave_fam_sz' : 'AVE_FAM_SZ',
    'hse_units' : 'HSE_UNITS',
    'vacant' : 'VACANT',
    'owner_occ' : 'OWNER_OCC',
    'renter_occ' : 'RENTER_OCC',
    'no_farms97' : 'NO_FARMS97',
    'avg_size97' : 'AVG_SIZE97',
    'crop_acr97' : 'CROP_ACR97',
    'avg_sale97' : 'AVG_SALE97',
    'sqmi' : 'SQMI',
    'oid' : 'OID',
    'geom' : 'MULTIPOLYGON',
    }

