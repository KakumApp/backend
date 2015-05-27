# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150320_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='created_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
    ]
