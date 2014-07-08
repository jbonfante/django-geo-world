# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WorldBorder'
        db.create_table('django_geo_world_worldborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('iso2', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('iso3', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('un', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2005', self.gf('django.db.models.fields.IntegerField')()),
            ('region', self.gf('django.db.models.fields.IntegerField')()),
            ('subregion', self.gf('django.db.models.fields.IntegerField')()),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('django_geo_world', ['WorldBorder'])

        # Adding index on 'WorldBorder', fields ['lat', 'lon']
        db.create_index('django_geo_world_worldborder', ['lat', 'lon'])

        # Adding model 'StateBorder'
        db.create_table('django_geo_world_stateborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state_fips', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('sub_region', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('state_abbr', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2007', self.gf('django.db.models.fields.IntegerField')()),
            ('pop00_sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('pop07_sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('white', self.gf('django.db.models.fields.IntegerField')()),
            ('black', self.gf('django.db.models.fields.IntegerField')()),
            ('ameri_es', self.gf('django.db.models.fields.IntegerField')()),
            ('asian', self.gf('django.db.models.fields.IntegerField')()),
            ('hawn_pi', self.gf('django.db.models.fields.IntegerField')()),
            ('other', self.gf('django.db.models.fields.IntegerField')()),
            ('mult_race', self.gf('django.db.models.fields.IntegerField')()),
            ('hispanic', self.gf('django.db.models.fields.IntegerField')()),
            ('males', self.gf('django.db.models.fields.IntegerField')()),
            ('females', self.gf('django.db.models.fields.IntegerField')()),
            ('age_under5', self.gf('django.db.models.fields.IntegerField')()),
            ('age_5_17', self.gf('django.db.models.fields.IntegerField')()),
            ('age_18_21', self.gf('django.db.models.fields.IntegerField')()),
            ('age_22_29', self.gf('django.db.models.fields.IntegerField')()),
            ('age_30_39', self.gf('django.db.models.fields.IntegerField')()),
            ('age_40_49', self.gf('django.db.models.fields.IntegerField')()),
            ('age_50_64', self.gf('django.db.models.fields.IntegerField')()),
            ('age_65_up', self.gf('django.db.models.fields.IntegerField')()),
            ('med_age', self.gf('django.db.models.fields.FloatField')()),
            ('med_age_m', self.gf('django.db.models.fields.FloatField')()),
            ('med_age_f', self.gf('django.db.models.fields.FloatField')()),
            ('households', self.gf('django.db.models.fields.IntegerField')()),
            ('ave_hh_sz', self.gf('django.db.models.fields.FloatField')()),
            ('hsehld_1_m', self.gf('django.db.models.fields.IntegerField')()),
            ('hsehld_1_f', self.gf('django.db.models.fields.IntegerField')()),
            ('marhh_chd', self.gf('django.db.models.fields.IntegerField')()),
            ('marhh_no_c', self.gf('django.db.models.fields.IntegerField')()),
            ('mhh_child', self.gf('django.db.models.fields.IntegerField')()),
            ('fhh_child', self.gf('django.db.models.fields.IntegerField')()),
            ('families', self.gf('django.db.models.fields.IntegerField')()),
            ('ave_fam_sz', self.gf('django.db.models.fields.FloatField')()),
            ('hse_units', self.gf('django.db.models.fields.IntegerField')()),
            ('vacant', self.gf('django.db.models.fields.IntegerField')()),
            ('owner_occ', self.gf('django.db.models.fields.IntegerField')()),
            ('renter_occ', self.gf('django.db.models.fields.IntegerField')()),
            ('no_farms97', self.gf('django.db.models.fields.FloatField')()),
            ('avg_size97', self.gf('django.db.models.fields.FloatField')()),
            ('crop_acr97', self.gf('django.db.models.fields.FloatField')()),
            ('avg_sale97', self.gf('django.db.models.fields.FloatField')()),
            ('sqmi', self.gf('django.db.models.fields.IntegerField')()),
            ('oid', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('django_geo_world', ['StateBorder'])

        # Adding model 'CityBorder'
        db.create_table('django_geo_world_cityborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('population', self.gf('django.db.models.fields.FloatField')()),
            ('capital', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPointField')()),
        ))
        db.send_create_signal('django_geo_world', ['CityBorder'])

        # Adding index on 'CityBorder', fields ['name', 'country']
        db.create_index('django_geo_world_cityborder', ['name', 'country'])

        # Adding model 'ZipcodeBorder'
        db.create_table('django_geo_world_zipcodeborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('po_name', self.gf('django.db.models.fields.CharField')(max_length=28)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('sumblkpop', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2007', self.gf('django.db.models.fields.IntegerField')()),
            ('pop07_sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('oid', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('django_geo_world', ['ZipcodeBorder'])

        # Adding index on 'ZipcodeBorder', fields ['zip', 'state']
        db.create_index('django_geo_world_zipcodeborder', ['zip', 'state'])

        # Adding model 'USCityBorder'
        db.create_table('django_geo_world_uscityborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('st_abbrev', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('place_fips', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('pop_2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2007', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('oid', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPointField')()),
        ))
        db.send_create_signal('django_geo_world', ['USCityBorder'])

        # Adding model 'UrbanBorder'
        db.create_table('django_geo_world_urbanborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ua_id', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('lsad', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('lsad_desc', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop00_sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('households', self.gf('django.db.models.fields.IntegerField')()),
            ('hse_units', self.gf('django.db.models.fields.IntegerField')()),
            ('sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('oid', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('django_geo_world', ['UrbanBorder'])

        # Adding model 'CountyBorder'
        db.create_table('django_geo_world_countyborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('state_fips', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('cnty_fips', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2007', self.gf('django.db.models.fields.IntegerField')()),
            ('pop00_sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('pop07_sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('white', self.gf('django.db.models.fields.IntegerField')()),
            ('black', self.gf('django.db.models.fields.IntegerField')()),
            ('ameri_es', self.gf('django.db.models.fields.IntegerField')()),
            ('asian', self.gf('django.db.models.fields.IntegerField')()),
            ('hawn_pi', self.gf('django.db.models.fields.IntegerField')()),
            ('other', self.gf('django.db.models.fields.IntegerField')()),
            ('mult_race', self.gf('django.db.models.fields.IntegerField')()),
            ('hispanic', self.gf('django.db.models.fields.IntegerField')()),
            ('males', self.gf('django.db.models.fields.IntegerField')()),
            ('females', self.gf('django.db.models.fields.IntegerField')()),
            ('age_under5', self.gf('django.db.models.fields.IntegerField')()),
            ('age_5_17', self.gf('django.db.models.fields.IntegerField')()),
            ('age_18_21', self.gf('django.db.models.fields.IntegerField')()),
            ('age_22_29', self.gf('django.db.models.fields.IntegerField')()),
            ('age_30_39', self.gf('django.db.models.fields.IntegerField')()),
            ('age_40_49', self.gf('django.db.models.fields.IntegerField')()),
            ('age_50_64', self.gf('django.db.models.fields.IntegerField')()),
            ('age_65_up', self.gf('django.db.models.fields.IntegerField')()),
            ('med_age', self.gf('django.db.models.fields.FloatField')()),
            ('med_age_m', self.gf('django.db.models.fields.FloatField')()),
            ('med_age_f', self.gf('django.db.models.fields.FloatField')()),
            ('households', self.gf('django.db.models.fields.IntegerField')()),
            ('ave_hh_sz', self.gf('django.db.models.fields.FloatField')()),
            ('hsehld_1_m', self.gf('django.db.models.fields.IntegerField')()),
            ('hsehld_1_f', self.gf('django.db.models.fields.IntegerField')()),
            ('marhh_chd', self.gf('django.db.models.fields.IntegerField')()),
            ('marhh_no_c', self.gf('django.db.models.fields.IntegerField')()),
            ('mhh_child', self.gf('django.db.models.fields.IntegerField')()),
            ('fhh_child', self.gf('django.db.models.fields.IntegerField')()),
            ('families', self.gf('django.db.models.fields.IntegerField')()),
            ('ave_fam_sz', self.gf('django.db.models.fields.FloatField')()),
            ('hse_units', self.gf('django.db.models.fields.IntegerField')()),
            ('vacant', self.gf('django.db.models.fields.IntegerField')()),
            ('owner_occ', self.gf('django.db.models.fields.IntegerField')()),
            ('renter_occ', self.gf('django.db.models.fields.IntegerField')()),
            ('no_farms97', self.gf('django.db.models.fields.FloatField')()),
            ('avg_size97', self.gf('django.db.models.fields.FloatField')()),
            ('crop_acr97', self.gf('django.db.models.fields.FloatField')()),
            ('avg_sale97', self.gf('django.db.models.fields.FloatField')()),
            ('sqmi', self.gf('django.db.models.fields.FloatField')()),
            ('oid', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('django_geo_world', ['CountyBorder'])

        # Adding index on 'CountyBorder', fields ['state_name', 'name']
        db.create_index('django_geo_world_countyborder', ['state_name', 'name'])

        # Adding model 'PlacePoint'
        db.create_table('django_geo_world_placepoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('place_class', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('st', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('stfips', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('placefip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('houseunits', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop_class', self.gf('django.db.models.fields.IntegerField')()),
            ('arealand', self.gf('django.db.models.fields.FloatField')()),
            ('areawater', self.gf('django.db.models.fields.FloatField')()),
            ('oid', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPointField')()),
        ))
        db.send_create_signal('django_geo_world', ['PlacePoint'])

        # Adding index on 'PlacePoint', fields ['st', 'name']
        db.create_index('django_geo_world_placepoint', ['st', 'name'])


    def backwards(self, orm):
        # Removing index on 'PlacePoint', fields ['st', 'name']
        db.delete_index('django_geo_world_placepoint', ['st', 'name'])

        # Removing index on 'CountyBorder', fields ['state_name', 'name']
        db.delete_index('django_geo_world_countyborder', ['state_name', 'name'])

        # Removing index on 'ZipcodeBorder', fields ['zip', 'state']
        db.delete_index('django_geo_world_zipcodeborder', ['zip', 'state'])

        # Removing index on 'CityBorder', fields ['name', 'country']
        db.delete_index('django_geo_world_cityborder', ['name', 'country'])

        # Removing index on 'WorldBorder', fields ['lat', 'lon']
        db.delete_index('django_geo_world_worldborder', ['lat', 'lon'])

        # Deleting model 'WorldBorder'
        db.delete_table('django_geo_world_worldborder')

        # Deleting model 'StateBorder'
        db.delete_table('django_geo_world_stateborder')

        # Deleting model 'CityBorder'
        db.delete_table('django_geo_world_cityborder')

        # Deleting model 'ZipcodeBorder'
        db.delete_table('django_geo_world_zipcodeborder')

        # Deleting model 'USCityBorder'
        db.delete_table('django_geo_world_uscityborder')

        # Deleting model 'UrbanBorder'
        db.delete_table('django_geo_world_urbanborder')

        # Deleting model 'CountyBorder'
        db.delete_table('django_geo_world_countyborder')

        # Deleting model 'PlacePoint'
        db.delete_table('django_geo_world_placepoint')


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