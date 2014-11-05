import unittest
from animal_class import Animal
from zoo_class import Zoo


class TestZoo(unittest.TestCase):
    def test_init(self):
        my_zoo = Zoo(50, 200)
        self.assertEqual(50, my_zoo.capacity)
        self.assertEqual(200, my_zoo.budget)

    def test_accommodate_empty_zoo(self):
        my_zoo = Zoo(50, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Leon", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        my_zoo.accommodate(animal2)
        self.assertIn(animal1, my_zoo.animals)
        self.assertIn(animal2, my_zoo.animals)

    def test_accommodate_animal_with_same_name_equal_species(self):
        my_zoo = Zoo(50, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        with self.assertRaises(ValueError):
            my_zoo.accommodate(animal2)
        self.assertIn(animal1, my_zoo.animals)
        self.assertNotIn(animal2, my_zoo.animals)

    def test_accommodate_animal_full_zoo(self):
        my_zoo = Zoo(1, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Leon", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        with self.assertRaises(ValueError):
            my_zoo.accommodate(animal2)
        self.assertIn(animal1, my_zoo.animals)
        self.assertNotIn(animal2, my_zoo.animals)

    def test_animal_count(self):
        my_zoo = Zoo(5, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Leon", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        my_zoo.accommodate(animal2)
        self.assertEqual(2, my_zoo.animals_count())

    def test_daily_incomes(self):
        my_zoo = Zoo(5, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Leon", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        my_zoo.accommodate(animal2)
        self.assertEqual(120, my_zoo.animals_count()*60)

    def test_daily_outcomes_meat_meat(self):
        my_zoo = Zoo(5, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Leon", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        my_zoo.accommodate(animal2)
        self.assertEqual(2.0, my_zoo.daily_outcomes())

    def test_daily_outcomes_meat_grass(self):
        my_zoo = Zoo(5, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Leon", 13, "Toshko", "male", 30, 180, "grass", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        my_zoo.accommodate(animal2)
        self.assertEqual(1.5, my_zoo.daily_outcomes())

    def test_daily_outcomes_grass_grass(self):
        my_zoo = Zoo(5, 10000)
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "grass", 3, 2, 90, 1.33, 0.25)
        animal2 = Animal("Leon", 13, "Toshko", "male", 30, 180, "grass", 3, 2, 90, 1.33, 0.25)
        my_zoo.accommodate(animal1)
        my_zoo.accommodate(animal2)
        self.assertEqual(1.0, my_zoo.daily_outcomes())






if __name__ == '__main__':
    unittest.main()