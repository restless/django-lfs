# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingmethod',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='name_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='note_en',
            field=models.TextField(null=True, verbose_name='Note', blank=True),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='note_pl',
            field=models.TextField(null=True, verbose_name='Note', blank=True),
        ),
    ]
