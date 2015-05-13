# python imports
from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from django.utils import translation

from lfs.catalog.models import Category
from lfs.catalog.models import Product
from lfs.core.models import Shop
from lfs.core.translation_utils import get_languages_list
from lfs.page.models import Page


class LFSLocaleSitemap(Sitemap):

    def __get(self, name, obj, default=None):
        try:
            attr = getattr(self, name)
        except AttributeError:
            return default
        if callable(attr):
            return attr(obj)
        return attr

    def get_urls(self, page=1, site=None, protocol=None):
        # Determine protocol
        if self.protocol is not None:
            protocol = self.protocol
        if protocol is None:
            protocol = 'http'

        # Determine domain
        if site is None:
            if Site._meta.installed:
                try:
                    site = Site.objects.get_current()
                except Site.DoesNotExist:
                    pass
            if site is None:
                raise ImproperlyConfigured("To use sitemaps, either enable the sites framework or pass a Site/RequestSite object in your view.")
        domain = site.domain

        current_language = translation.get_language()

        urls = []
        for item in self.paginator.page(page).object_list:
            alternates = []
            for lang in get_languages_list():
                translation.activate(lang)
                alt_loc = "%s://%s%s" % (protocol, domain, self.__get('location', item))
                alternates.append({'lang': lang,
                                   'loc': alt_loc})

            for lang in get_languages_list():
                translation.activate(lang)

                loc = "%s://%s%s" % (protocol, domain, self.__get('location', item))

                priority = self.__get('priority', item, None)
                url_info = {
                    'item':       item,
                    'location':   loc,
                    'alternates': alternates,
                    'lastmod':    self.__get('lastmod', item, None),
                    'changefreq': self.__get('changefreq', item, None),
                    'priority':   str(priority is not None and priority or ''),
                }
                urls.append(url_info)
            translation.activate(current_language)
        return urls


class ProductSitemap(LFSLocaleSitemap):
    """Google's XML sitemap for products.
    """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.filter(active=True).exclude(sub_type=2, parent__active=False)

    def lastmod(self, obj):
        return obj.creation_date


class CategorySitemap(LFSLocaleSitemap):
    """Google's XML sitemap for products.
    """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return datetime.now()


class PageSitemap(LFSLocaleSitemap):
    """Google's XML sitemap for pages.
    """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Page.objects.filter(active=True)

    def lastmod(self, obj):
        return datetime.now()


class ShopSitemap(LFSLocaleSitemap):
    """Google's XML sitemap for the shop.
    """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Shop.objects.all()

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return '/'
