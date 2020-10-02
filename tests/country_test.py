import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country1 = Country("Finland")

    def test_country_has_name(self):
        self.assertEqual("Finland", self.country1.name)
