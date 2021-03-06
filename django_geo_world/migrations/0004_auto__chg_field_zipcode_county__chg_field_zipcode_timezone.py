# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Zipcode.county'
        db.alter_column('django_geo_world_zipcode', 'county', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Zipcode.timezone'
        db.alter_column('django_geo_world_zipcode', 'timezone', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Zipcode.county'
        db.alter_column('django_geo_world_zipcode', 'county', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Zipcode.timezone'
        db.alter_column('django_geo_world_zipcode', 'timezone', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        'django_geo_world.cityborder': {
            'Meta': {'ordering': "['name', 'country']", 'object_name': 'CityBorder', 'index_together': "[['name', 'country']]"},
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'population': ('django.db.models.fields.FloatField', [], {})
        },
        'django_geo_world.countyborder': {
            'Meta': {'ordering': "['state_name', 'name']", 'object_name': 'CountyBorder', 'index_together': "[['state_name', 'name']]"},
            'age_18_21': ('django.db.models.fields.IntegerField', [], {}),
            'age_22_29': ('django.db.models.fields.IntegerField', [], {}),
            'age_30_39': ('django.db.models.fields.IntegerField', [], {}),
            'age_40_49': ('django.db.models.fields.IntegerField', [], {}),
            'age_50_64': ('django.db.models.fields.IntegerField', [], {}),
            'age_5_17': ('django.db.models.fields.IntegerField', [], {}),
            'age_65_up': ('django.db.models.fields.IntegerField', [], {}),
            'age_under5': ('django.db.models.fields.IntegerField', [], {}),
            'ameri_es': ('django.db.models.fields.IntegerField', [], {}),
            'asian': ('django.db.models.fields.IntegerField', [], {}),
            'ave_fam_sz': ('django.db.models.fields.FloatField', [], {}),
            'ave_hh_sz': ('django.db.models.fields.FloatField', [], {}),
            'avg_sale97': ('django.db.models.fields.FloatField', [], {}),
            'avg_size97': ('django.db.models.fields.FloatField', [], {}),
            'black': ('django.db.models.fields.IntegerField', [], {}),
            'cnty_fips': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'crop_acr97': ('django.db.models.fields.FloatField', [], {}),
            'families': ('django.db.models.fields.IntegerField', [], {}),
            'females': ('django.db.models.fields.IntegerField', [], {}),
            'fhh_child': ('django.db.models.fields.IntegerField', [], {}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'hawn_pi': ('django.db.models.fields.IntegerField', [], {}),
            'hispanic': ('django.db.models.fields.IntegerField', [], {}),
            'households': ('django.db.models.fields.IntegerField', [], {}),
            'hse_units': ('django.db.models.fields.IntegerField', [], {}),
            'hsehld_1_f': ('django.db.models.fields.IntegerField', [], {}),
            'hsehld_1_m': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'males': ('django.db.models.fields.IntegerField', [], {}),
            'marhh_chd': ('django.db.models.fields.IntegerField', [], {}),
            'marhh_no_c': ('django.db.models.fields.IntegerField', [], {}),
            'med_age': ('django.db.models.fields.FloatField', [], {}),
            'med_age_f': ('django.db.models.fields.FloatField', [], {}),
            'med_age_m': ('django.db.models.fields.FloatField', [], {}),
            'mhh_child': ('django.db.models.fields.IntegerField', [], {}),
            'mult_race': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'no_farms97': ('django.db.models.fields.FloatField', [], {}),
            'oid': ('django.db.models.fields.IntegerField', [], {}),
            'other': ('django.db.models.fields.IntegerField', [], {}),
            'owner_occ': ('django.db.models.fields.IntegerField', [], {}),
            'pop00_sqmi': ('django.db.models.fields.FloatField', [], {}),
            'pop07_sqmi': ('django.db.models.fields.FloatField', [], {}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2007': ('django.db.models.fields.IntegerField', [], {}),
            'renter_occ': ('django.db.models.fields.IntegerField', [], {}),
            'sqmi': ('django.db.models.fields.FloatField', [], {}),
            'state_fips': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'vacant': ('django.db.models.fields.IntegerField', [], {}),
            'white': ('django.db.models.fields.IntegerField', [], {})
        },
        'django_geo_world.placepoint': {
            'Meta': {'ordering': "['st', 'name']", 'object_name': 'PlacePoint', 'index_together': "[['st', 'name']]"},
            'arealand': ('django.db.models.fields.FloatField', [], {}),
            'areawater': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPointField', [], {}),
            'houseunits': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'oid': ('django.db.models.fields.IntegerField', [], {}),
            'place_class': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'placefip': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop_class': ('django.db.models.fields.IntegerField', [], {}),
            'st': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'stfips': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'django_geo_world.stateborder': {
            'Meta': {'ordering': "['state_name']", 'object_name': 'StateBorder'},
            'age_18_21': ('django.db.models.fields.IntegerField', [], {}),
            'age_22_29': ('django.db.models.fields.IntegerField', [], {}),
            'age_30_39': ('django.db.models.fields.IntegerField', [], {}),
            'age_40_49': ('django.db.models.fields.IntegerField', [], {}),
            'age_50_64': ('django.db.models.fields.IntegerField', [], {}),
            'age_5_17': ('django.db.models.fields.IntegerField', [], {}),
            'age_65_up': ('django.db.models.fields.IntegerField', [], {}),
            'age_under5': ('django.db.models.fields.IntegerField', [], {}),
            'ameri_es': ('django.db.models.fields.IntegerField', [], {}),
            'asian': ('django.db.models.fields.IntegerField', [], {}),
            'ave_fam_sz': ('django.db.models.fields.FloatField', [], {}),
            'ave_hh_sz': ('django.db.models.fields.FloatField', [], {}),
            'avg_sale97': ('django.db.models.fields.FloatField', [], {}),
            'avg_size97': ('django.db.models.fields.FloatField', [], {}),
            'black': ('django.db.models.fields.IntegerField', [], {}),
            'crop_acr97': ('django.db.models.fields.FloatField', [], {}),
            'families': ('django.db.models.fields.IntegerField', [], {}),
            'females': ('django.db.models.fields.IntegerField', [], {}),
            'fhh_child': ('django.db.models.fields.IntegerField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'hawn_pi': ('django.db.models.fields.IntegerField', [], {}),
            'hispanic': ('django.db.models.fields.IntegerField', [], {}),
            'households': ('django.db.models.fields.IntegerField', [], {}),
            'hse_units': ('django.db.models.fields.IntegerField', [], {}),
            'hsehld_1_f': ('django.db.models.fields.IntegerField', [], {}),
            'hsehld_1_m': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'males': ('django.db.models.fields.IntegerField', [], {}),
            'marhh_chd': ('django.db.models.fields.IntegerField', [], {}),
            'marhh_no_c': ('django.db.models.fields.IntegerField', [], {}),
            'med_age': ('django.db.models.fields.FloatField', [], {}),
            'med_age_f': ('django.db.models.fields.FloatField', [], {}),
            'med_age_m': ('django.db.models.fields.FloatField', [], {}),
            'mhh_child': ('django.db.models.fields.IntegerField', [], {}),
            'mult_race': ('django.db.models.fields.IntegerField', [], {}),
            'no_farms97': ('django.db.models.fields.FloatField', [], {}),
            'oid': ('django.db.models.fields.IntegerField', [], {}),
            'other': ('django.db.models.fields.IntegerField', [], {}),
            'owner_occ': ('django.db.models.fields.IntegerField', [], {}),
            'pop00_sqmi': ('django.db.models.fields.FloatField', [], {}),
            'pop07_sqmi': ('django.db.models.fields.FloatField', [], {}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2007': ('django.db.models.fields.IntegerField', [], {}),
            'renter_occ': ('django.db.models.fields.IntegerField', [], {}),
            'sqmi': ('django.db.models.fields.IntegerField', [], {}),
            'state_abbr': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_fips': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sub_region': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vacant': ('django.db.models.fields.IntegerField', [], {}),
            'white': ('django.db.models.fields.IntegerField', [], {})
        },
        'django_geo_world.urbanborder': {
            'Meta': {'ordering': "['name']", 'object_name': 'UrbanBorder'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'households': ('django.db.models.fields.IntegerField', [], {}),
            'hse_units': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lsad': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'lsad_desc': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'oid': ('django.db.models.fields.IntegerField', [], {}),
            'pop00_sqmi': ('django.db.models.fields.FloatField', [], {}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'sqmi': ('django.db.models.fields.FloatField', [], {}),
            'ua_id': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'django_geo_world.uscityborder': {
            'Meta': {'ordering': "['st_abbrev', 'name']", 'object_name': 'USCityBorder'},
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'oid': ('django.db.models.fields.IntegerField', [], {}),
            'place_fips': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'pop2007': ('django.db.models.fields.IntegerField', [], {}),
            'pop_2000': ('django.db.models.fields.IntegerField', [], {}),
            'st_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'django_geo_world.worldborder': {
            'Meta': {'ordering': "['name']", 'object_name': 'WorldBorder', 'index_together': "[['lat', 'lon']]"},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso2': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pop2005': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.IntegerField', [], {}),
            'subregion': ('django.db.models.fields.IntegerField', [], {}),
            'un': ('django.db.models.fields.IntegerField', [], {})
        },
        'django_geo_world.zipcode': {
            'Meta': {'object_name': 'Zipcode'},
            'acceptable_cities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'area_codes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'decommissioned': ('django.db.models.fields.BooleanField', [], {}),
            'estimated_population': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'primary_city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'STANDARD'", 'max_length': '20'}),
            'unacceptable_cities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'world_region': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'django_geo_world.zipcodeborder': {
            'Meta': {'ordering': "['zip']", 'object_name': 'ZipcodeBorder', 'index_together': "[['zip', 'state']]"},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oid': ('django.db.models.fields.IntegerField', [], {}),
            'po_name': ('django.db.models.fields.CharField', [], {'max_length': '28'}),
            'pop07_sqmi': ('django.db.models.fields.FloatField', [], {}),
            'pop2007': ('django.db.models.fields.IntegerField', [], {}),
            'sqmi': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'sumblkpop': ('django.db.models.fields.IntegerField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['django_geo_world']