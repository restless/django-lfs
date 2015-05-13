# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='body_pl',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='file_en',
            field=models.FileField(upload_to=b'files', null=True, verbose_name='File', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='file_pl',
            field=models.FileField(upload_to=b'files', null=True, verbose_name='File', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_description_en',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_description_pl',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_keywords_en',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_keywords_pl',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_title_en',
            field=models.CharField(default=b'<title>', max_length=80, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_title_pl',
            field=models.CharField(default=b'<title>', max_length=80, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='short_text_en',
            field=models.TextField(null=True, verbose_name='Short text', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='short_text_pl',
            field=models.TextField(null=True, verbose_name='Short text', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='slug_en',
            field=models.SlugField(max_length=100, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='page',
            name='slug_pl',
            field=models.SlugField(max_length=100, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug'),
        ),
    ]
