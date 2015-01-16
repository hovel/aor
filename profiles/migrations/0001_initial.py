# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import pybb.util
import django.core.validators
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.TextField(max_length=1024, verbose_name='Signature', blank=True)),
                ('signature_html', models.TextField(max_length=1054, verbose_name='Signature HTML Version', blank=True)),
                ('time_zone', models.FloatField(default=3.0, verbose_name='Time zone', choices=[(-12.0, b'-12'), (-11.0, b'-11'), (-10.0, b'-10'), (-9.5, b'-09.5'), (-9.0, b'-09'), (-8.5, b'-08.5'), (-8.0, b'-08 PST'), (-7.0, b'-07 MST'), (-6.0, b'-06 CST'), (-5.0, b'-05 EST'), (-4.0, b'-04 AST'), (-3.5, b'-03.5'), (-3.0, b'-03 ADT'), (-2.0, b'-02'), (-1.0, b'-01'), (0.0, b'00 GMT'), (1.0, b'+01 CET'), (2.0, b'+02'), (3.0, b'+03'), (3.5, b'+03.5'), (4.0, b'+04'), (4.5, b'+04.5'), (5.0, b'+05'), (5.5, b'+05.5'), (6.0, b'+06'), (6.5, b'+06.5'), (7.0, b'+07'), (8.0, b'+08'), (9.0, b'+09'), (9.5, b'+09.5'), (10.0, b'+10'), (10.5, b'+10.5'), (11.0, b'+11'), (11.5, b'+11.5'), (12.0, b'+12'), (13.0, b'+13'), (14.0, b'+14')])),
                ('language', models.CharField(default=b'ru-RU', max_length=10, verbose_name='Language', blank=True, choices=[(b'ru', b'Russian'), (b'ua', b'Ukraine')])),
                ('show_signatures', models.BooleanField(default=True, verbose_name='Show signatures')),
                ('post_count', models.IntegerField(default=0, verbose_name='Post count', blank=True)),
                ('avatar', sorl.thumbnail.fields.ImageField(upload_to=pybb.util.FilePathGenerator(to=b'pybb/avatar'), null=True, verbose_name='Avatar', blank=True)),
                ('autosubscribe', models.BooleanField(default=False, help_text='Automatically subscribe to topics that you answer', verbose_name='Automatically subscribe')),
                ('theme', models.CharField(default=b'default', max_length=32, choices=[(b'default', 'default theme'), (b'dark', 'dark theme')])),
                ('date_show_type', models.IntegerField(default=2, verbose_name='Date show type', choices=[(2, 'Reverted'), (1, 'Classic')])),
                ('icq', models.CharField(blank=True, max_length=10, null=True, verbose_name='ICQ Number', validators=[django.core.validators.RegexValidator(regex=b'\\d+')])),
                ('skype', models.CharField(max_length=100, null=True, verbose_name='Skype username', blank=True)),
                ('jabber', models.CharField(max_length=100, null=True, verbose_name='Jabber address', blank=True)),
                ('site', models.URLField(null=True, verbose_name='Personal site', blank=True)),
                ('interests', models.TextField(null=True, verbose_name='Interests', blank=True)),
                ('user', annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
            bases=(models.Model,),
        ),
    ]
