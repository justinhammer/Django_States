# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151012_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state_map',
            field=models.ImageField(default=1, upload_to=b'state_map'),
            preserve_default=False,
        ),
    ]
