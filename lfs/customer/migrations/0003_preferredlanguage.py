# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_set_null_to_address_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferredLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default='en-us', max_length=5, verbose_name='Preferred language')),
                ('user', models.OneToOneField(related_name='preferred_language', verbose_name='Customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
