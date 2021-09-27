import unittest

from . import test_get_provinces

loader = unittest.TestLoader()

suite = unittest.TestSuite(
    loader.loadTestsFromModule(test_get_provinces)
)