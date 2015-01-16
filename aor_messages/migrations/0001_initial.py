# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AorMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body_html', models.TextField()),
                ('message', annoying.fields.AutoOneToOneField(related_name='aor_message', to='postman.Message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
