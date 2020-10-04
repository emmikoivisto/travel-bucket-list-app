import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City("Helsinki", False)

    def test_city_has_name(self):
        self.assertEqual("Helsinki", self.city.name)

    def test_can_mark_visited(self):
        self.city.mark_visited()
        self.assertEqual(True, self.city.visited)

    def test_city_has_been_visited(self):
        self.assertEqual(False, self.city.visited)

