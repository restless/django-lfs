# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='name_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='note_en',
            field=models.TextField(null=True, verbose_name='note', blank=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='note_pl',
            field=models.TextField(null=True, verbose_name='note', blank=True),
        ),
    ]
