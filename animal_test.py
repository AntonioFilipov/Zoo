import unittest
from animal_class import Animal


class TestAnimalClass(unittest.TestCase):

    def test_init(self):
        animal1 = Animal("Tiger", "13", "Toshko", "male", "30", 15*12, "meat",
            3, 2, 90, 1.33, 0.25)
