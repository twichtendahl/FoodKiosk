import unittest
from size import Size
from item import Item
from customization import Customization
from customizedItem import CustomizedItem

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item(1, "cheeseburger")

    def test_string(self):
        self.assertEqual(str(self.item), str(self.item.number) + ": " + self.item.name)

    def test_getItemNumber(self):
        self.assertEqual(self.item.getNumber(), 1)

class CustomizedItemTest(unittest.TestCase):
    def setUp(self):
        self.customizedItem = CustomizedItem(self, 1, "cheeseburger", Size("no size"), 5.99, Customization("no pickles", 0))
    
    def test_size(self):
        self.assertEqual(self.customizedItem.getSize, Size("no size"))