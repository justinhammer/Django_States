# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AddField(
            model_name='state',
            name='pop',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
