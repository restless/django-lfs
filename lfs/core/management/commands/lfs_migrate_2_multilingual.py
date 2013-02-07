from django.core.management.base import BaseCommand

# south imports
from south.db import db


class Command(BaseCommand):
    args = ''
    help = 'Migrations for multilingual LFS'

    def handle(self, *args, **options):
        """
        """
        db.delete_unique("catalog_category", "slug")
        db.delete_unique("catalog_product", "slug")
        db.delete_unique("page_page", "slug")
