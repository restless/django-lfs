# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='averageratingportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='averageratingportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='cartportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='cartportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='categoriesportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='categoriesportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='deliverytimeportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='deliverytimeportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='featuredportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='featuredportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='filterportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='filterportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='forsaleportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='forsaleportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='latestportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='latestportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='pagesportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='pagesportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='recentproductsportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='recentproductsportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='relatedproductsportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='relatedproductsportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='textportlet',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
        ),
        migrations.AddField(
            model_name='textportlet',
            name='text_pl',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
        ),
        migrations.AddField(
            model_name='textportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='textportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='topsellerportlet',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='topsellerportlet',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
        ),
    ]
