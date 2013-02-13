# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'World.level'
        db.delete_column('game_world', 'level')


    def backwards(self, orm):
        # Adding field 'World.level'
        db.add_column('game_world', 'level',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 2, 13, 0, 0), max_length=200),
                      keep_default=False)


    models = {
        'game.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'riddle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Riddle']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'game.hint': {
            'Meta': {'object_name': 'Hint'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'riddle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Riddle']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'game.riddle': {
            'Meta': {'object_name': 'Riddle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'world': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.World']"})
        },
        'game.world': {
            'Meta': {'object_name': 'World'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['game']