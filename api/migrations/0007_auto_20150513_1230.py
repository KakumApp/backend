# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_target_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='photo',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
