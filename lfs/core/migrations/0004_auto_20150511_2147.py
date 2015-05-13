# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lfs.core.fields.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150511_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='link_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Link', blank=True),
        ),
        migrations.AddField(
            model_name='action',
            name='link_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Link', blank=True),
        ),
        migrations.AddField(
            model_name='action',
            name='title_en',
            field=models.CharField(max_length=40, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='action',
            name='title_pl',
            field=models.CharField(max_length=40, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='actiongroup',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AddField(
            model_name='actiongroup',
            name='name_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='shop',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='image_en',
            field=lfs.core.fields.thumbs.ImageWithThumbsField(upload_to=b'images', null=True, verbose_name='Image', sizes=((60, 60), (100, 100), (200, 200), (400, 400)), blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='image_pl',
            field=lfs.core.fields.thumbs.ImageWithThumbsField(upload_to=b'images', null=True, verbose_name='Image', sizes=((60, 60), (100, 100), (200, 200), (400, 400)), blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='meta_description_en',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='meta_description_pl',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='meta_keywords_en',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='meta_keywords_pl',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='meta_title_en',
            field=models.CharField(default=b'<name>', max_length=80, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='meta_title_pl',
            field=models.CharField(default=b'<name>', max_length=80, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='name_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='shop',
            name='name_pl',
            field=models.CharField(max_length=30, null=True, verbose_name='Name'),
        ),
    ]
