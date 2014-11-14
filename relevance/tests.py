from django.test import TestCase
from .models import JSONStore


class JSONStoreTests(TestCase):
    """
    Class for tests for JSONStore Model
    """
    def test_books_property_unit_test(self):
        """
        tests that it returns correct dict
        """
        json_store = JSONStore()
        # self.assertIsInstance(json_store.books, dict)
        # self.assertEqual(?, ?)
        self.assertRaises(NotImplementedError, lambda: json_store.books)

    def test_books_property_integration_test(self):
        """
        tests property with call to db
        """
        json_store = JSONStore.objects.first()
        self.assertIsNone(json_store)
