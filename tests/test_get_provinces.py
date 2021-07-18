import unittest

from src import get_provinces

class TestGetProvinceMethods(unittest.TestCase):

    def test_all_provinces(self):
        self.assertEqual(get_provinces(), ['Kigali'])

    def test_number_of_provinces(self):
        self.assertEqual(len(get_provinces()), 1)