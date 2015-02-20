# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.ForeignKey(related_name='places', to='api.Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='target',
            name='other_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
