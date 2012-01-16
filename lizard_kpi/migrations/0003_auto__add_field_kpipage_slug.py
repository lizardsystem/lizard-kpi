# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'KPIPage.slug'
        db.add_column('lizard_kpi_kpipage', 'slug', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'KPIPage.slug'
        db.delete_column('lizard_kpi_kpipage', 'slug')


    models = {
        'lizard_kpi.kpi': {
            'Meta': {'ordering': "('kpi_page', 'order')", 'object_name': 'KPI'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kpi_page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_kpi.KPIPage']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'lizard_kpi.kpipage': {
            'Meta': {'ordering': "('name',)", 'object_name': 'KPIPage'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lizard_kpi']
