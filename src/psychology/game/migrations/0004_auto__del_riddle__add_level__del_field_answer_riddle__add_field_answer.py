# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Riddle'
        db.delete_table('game_riddle')

        # Adding model 'Level'
        db.create_table('game_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('world', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.World'])),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('game', ['Level'])

        # Deleting field 'Answer.riddle'
        db.delete_column('game_answer', 'riddle_id')

        # Adding field 'Answer.level'
        db.add_column('game_answer', 'level',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['game.Level']),
                      keep_default=False)

        # Deleting field 'Hint.riddle'
        db.delete_column('game_hint', 'riddle_id')

        # Adding field 'Hint.level'
        db.add_column('game_hint', 'level',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['game.Level']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Riddle'
        db.create_table('game_riddle', (
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('world', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.World'])),
        ))
        db.send_create_signal('game', ['Riddle'])

        # Deleting model 'Level'
        db.delete_table('game_level')

        # Adding field 'Answer.riddle'
        db.add_column('game_answer', 'riddle',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['game.Riddle']),
                      keep_default=False)

        # Deleting field 'Answer.level'
        db.delete_column('game_answer', 'level_id')

        # Adding field 'Hint.riddle'
        db.add_column('game_hint', 'riddle',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['game.Riddle']),
                      keep_default=False)

        # Deleting field 'Hint.level'
        db.delete_column('game_hint', 'level_id')


    models = {
        'game.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Level']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'game.hint': {
            'Meta': {'object_name': 'Hint'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['game.Level']"}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'game.level': {
            'Meta': {'object_name': 'Level'},
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