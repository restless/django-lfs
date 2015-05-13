# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150428_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiongroup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name', blank=True),
        ),
    ]
