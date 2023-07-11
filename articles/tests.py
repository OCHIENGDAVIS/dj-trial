from django.test import TestCase
from django.conf import settings


class ArticleTest(TestCase):
    def test_secret_key_strength(self):
        key = settings.SECRET_KEY
        self.assertTrue(len(key) >= 8)
