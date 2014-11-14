from django.test import TestCase
from .models import JSONStore


class JSONStoreTests(TestCase):
    """
    Class for tests for JSONStore Model
    """
    def test_books_property(self):
        """
        tests that it returns correct dict
        """
        json_store = JSONStore()
        # self.assertIsInstance(json_store.books, dict)
        self.assertRaises(NotImplementedError, lambda: json_store.books)
