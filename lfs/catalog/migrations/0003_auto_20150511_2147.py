# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lfs.core.fields.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20150427_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image_en',
            field=lfs.core.fields.thumbs.ImageWithThumbsField(upload_to=b'images', null=True, verbose_name='Image', sizes=((60, 60), (100, 100), (200, 200), (300, 300), (400, 400)), blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image_pl',
            field=lfs.core.fields.thumbs.ImageWithThumbsField(upload_to=b'images', null=True, verbose_name='Image', sizes=((60, 60), (100, 100), (200, 200), (300, 300), (400, 400)), blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description_en',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description_pl',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords_en',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords_pl',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title_en',
            field=models.CharField(default=b'<name>', max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title_pl',
            field=models.CharField(default=b'<name>', max_length=100, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='Short description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='short_description_pl',
            field=models.TextField(null=True, verbose_name='Short description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(unique=True, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_pl',
            field=models.SlugField(unique=True, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='deliverytime',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='deliverytime',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description_en',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description_pl',
            field=models.TextField(null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords_en',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords_pl',
            field=models.TextField(null=True, verbose_name='Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title_en',
            field=models.CharField(default=b'<name>', max_length=80, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title_pl',
            field=models.CharField(default=b'<name>', max_length=80, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(help_text='The name of the product.', max_length=80, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_pl',
            field=models.CharField(help_text='The name of the product.', max_length=80, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='Short description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_pl',
            field=models.TextField(null=True, verbose_name='Short description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_en',
            field=models.SlugField(null=True, max_length=120, help_text="The unique last part of the Product's URL.", unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_pl',
            field=models.SlugField(null=True, max_length=120, help_text="The unique last part of the Product's URL.", unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='productpropertyvalue',
            name='value_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Value', blank=True),
        ),
        migrations.AddField(
            model_name='productpropertyvalue',
            name='value_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Value', blank=True),
        ),
        migrations.AddField(
            model_name='property',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='property',
            name='name_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='property',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='property',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='propertyoption',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='propertyoption',
            name='name_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='staticblock',
            name='html_en',
            field=models.TextField(null=True, verbose_name='HTML', blank=True),
        ),
        migrations.AddField(
            model_name='staticblock',
            name='html_pl',
            field=models.TextField(null=True, verbose_name='HTML', blank=True),
        ),
        migrations.AddField(
            model_name='staticblock',
            name='name_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='staticblock',
            name='name_pl',
            field=models.CharField(max_length=30, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(related_name='product_set', blank=True, to='lfs.Supplier', null=True),
        ),
    ]
