# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'World'
        db.create_table('game_world', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('game', ['World'])

        # Adding model 'Riddle'
        db.create_table('game_riddle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('world', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.World'])),
            ('question', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('game', ['Riddle'])

        # Adding model 'Hint'
        db.create_table('game_hint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('riddle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Riddle'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('game', ['Hint'])

        # Adding model 'Answer'
        db.create_table('game_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('riddle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Riddle'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('game', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'World'
        db.delete_table('game_world')

        # Deleting model 'Riddle'
        db.delete_table('game_riddle')

        # Deleting model 'Hint'
        db.delete_table('game_hint')

        # Deleting model 'Answer'
        db.delete_table('game_answer')


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
            'question': ('django.db.models.fields.TextField', [], {}),
            'world': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.World']"})
        },
        'game.world': {
            'Meta': {'object_name': 'World'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
        }
    }

    complete_apps = ['game']