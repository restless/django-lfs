from django.core.management.base import BaseCommand
from django.db import models, migrations


class Command(BaseCommand):
    args = ''
    help = 'Migrations for multilingual LFS'

    def handle(self, *args, **options):
        """
        """
        migrations.AlterField(
            model_name='catalog_category',
            name='slug',
            field=models.SlugField(unique=False, verbose_name='Slug'))
        migrations.AlterField(
            model_name='catalog_product',
            name='slug',
            field=models.SlugField(help_text="The unique last part of the Product's URL.", unique=False, max_length=120, verbose_name='Slug'))
        migrations.AlterField(
            model_name='page_page',
            name='slug',
            field=models.SlugField(unique=False, max_length=100, verbose_name='Slug'))
