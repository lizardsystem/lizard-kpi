# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'KPI'
        db.create_table('lizard_kpi_kpi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('lizard_kpi', ['KPI'])


    def backwards(self, orm):
        
        # Deleting model 'KPI'
        db.delete_table('lizard_kpi_kpi')


    models = {
        'lizard_kpi.kpi': {
            'Meta': {'object_name': 'KPI'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['lizard_kpi']
