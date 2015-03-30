# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_intermediary_meetingpoint_meetingtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='other_name',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
