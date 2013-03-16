# django imports
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from lfs.catalog.models import Category

from lfs.page.models import Page


class ManageTestCase(TestCase):
    """Tests manage interface
    """
    fixtures = ['lfs_shop.xml', "lfs_user.xml"]

    def setUp(self):
        for i in range(1, 4):
            cat, created = Category.objects.get_or_create(pk=i, name="cat" + str(i), slug="cat" + str(i), position=10, parent=None)

    # def test_category_sorting(self):
    #     """
    #     Test we get correct sorting of categories from json api
    #     """
    #
    #     self.assertEqual(3, Category.objects.count())
    #     csv = CategorySortView()
    #
    #     js = 'category[3]=root&category[1]=root&category[2]=1'
    #     csv.sort_categories(js)
    #     cat1 = Category.objects.get(pk=1)
    #     cat2 = Category.objects.get(pk=2)
    #     cat3 = Category.objects.get(pk=3)
    #
    #     # check positions are correct
    #     self.assertEqual(cat1.position, 20)
    #     self.assertEqual(cat2.position, 30)
    #     self.assertEqual(cat3.position, 10)
    #
    #     # check parents are correct
    #     self.assertEqual(cat1.parent, None)
    #     self.assertEqual(cat2.parent, cat1)
    #     self.assertEqual(cat3.parent, None)
    #
    #     js = 'category[1]=root&category[2]=root&category[3]=2'
    #     csv.sort_categories(js)
    #     cat1 = Category.objects.get(pk=1)
    #     cat2 = Category.objects.get(pk=2)
    #     cat3 = Category.objects.get(pk=3)
    #
    #     # check positions are correct
    #     self.assertEqual(cat1.position, 10)
    #     self.assertEqual(cat2.position, 20)
    #     self.assertEqual(cat3.position, 30)
    #
    #     # check parents are correct
    #     self.assertEqual(cat1.parent, None)
    #     self.assertEqual(cat2.parent, None)
    #     self.assertEqual(cat3.parent, cat2)

    def test_add_page_with_existing_slug(self):
        self.client.login(username="admin", password="admin")
        self.user = User.objects.get(username="admin")

        Page.objects.create(title="Test1", slug="test")
        page_count = Page.objects.count()
        response = self.client.post(reverse('lfs_add_page'), {'title': 'Test2', 'slug': 'test'})
        self.assertEqual(page_count, Page.objects.count())
        self.assertTrue('slug' in response.context['form'].errors)
        self.assertTrue('already exists' in response.context['form'].errors['slug'][0])
