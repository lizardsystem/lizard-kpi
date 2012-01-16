# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'KPIPage'
        db.create_table('lizard_kpi_kpipage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('lizard_kpi', ['KPIPage'])

        # Adding field 'KPI.kpi_page'
        db.add_column('lizard_kpi_kpi', 'kpi_page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_kpi.KPIPage'], null=True, blank=True), keep_default=False)

        # Adding field 'KPI.order'
        db.add_column('lizard_kpi_kpi', 'order', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'KPIPage'
        db.delete_table('lizard_kpi_kpipage')

        # Deleting field 'KPI.kpi_page'
        db.delete_column('lizard_kpi_kpi', 'kpi_page_id')

        # Deleting field 'KPI.order'
        db.delete_column('lizard_kpi_kpi', 'order')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lizard_kpi']
