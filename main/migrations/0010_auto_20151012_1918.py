# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_state_state_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='state_map',
            field=models.ImageField(null=True, upload_to=b'state_map', blank=True),
        ),
    ]
