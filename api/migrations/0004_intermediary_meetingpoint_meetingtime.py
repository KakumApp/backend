# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150220_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intermediary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('other_name', models.CharField(max_length=50, null=True)),
                ('phone_no', models.CharField(max_length=20)),
                ('photo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeetingPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('gps_lat', models.CharField(max_length=50)),
                ('gps_long', models.CharField(max_length=50)),
                ('photo', models.TextField()),
                ('intermediary', models.ForeignKey(related_name='meeting_points', to='api.Intermediary')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeetingTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=20)),
                ('begin', models.CharField(max_length=10)),
                ('end', models.CharField(max_length=10)),
                ('meeting_point', models.ForeignKey(related_name='meeting_times', to='api.MeetingPoint')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
