# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AorMessage'
        db.create_table(u'aor_messages_aormessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('annoying.fields.AutoOneToOneField')(related_name=u'aor_message', unique=True, to=orm['postman.Message'])),
            ('body_html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'aor_messages', ['AorMessage'])


    def backwards(self, orm):
        # Deleting model 'AorMessage'
        db.delete_table(u'aor_messages_aormessage')


    models = {
        u'aor_messages.aormessage': {
            'Meta': {'object_name': 'AorMessage'},
            'body_html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('annoying.fields.AutoOneToOneField', [], {'related_name': "u'aor_message'", 'unique': 'True', 'to': u"orm['postman.Message']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'postman.message': {
            'Meta': {'ordering': "[u'-sent_at', u'-id']", 'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderation_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'moderated_messages'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'moderation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'moderation_reason': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'moderation_status': ('django.db.models.fields.CharField', [], {'default': "u'p'", 'max_length': '1'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'next_messages'", 'null': 'True', 'to': u"orm['postman.Message']"}),
            'read_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'received_messages'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'recipient_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recipient_deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'replied_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'sent_messages'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'sender_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender_deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'child_messages'", 'null': 'True', 'to': u"orm['postman.Message']"})
        }
    }

    complete_apps = ['aor_messages']