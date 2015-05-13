# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0002_auto_20150428_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='meta_description_en',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='meta_description_pl',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='meta_keywords_en',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='meta_keywords_pl',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='meta_title_en',
            field=models.CharField(default=b'<name>', max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='meta_title_pl',
            field=models.CharField(default=b'<name>', max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='Short description', blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='short_description_pl',
            field=models.TextField(null=True, verbose_name='Short description', blank=True),
        ),
    ]
