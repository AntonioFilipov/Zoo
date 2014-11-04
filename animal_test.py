import unittest
from animal_class import Animal


class TestAnimalClass(unittest.TestCase):

    def test_animal_init(self):
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        self.assertEqual(animal1.species, "Tiger")
        self.assertEqual(animal1.age, 13)
        self.assertEqual(animal1.name, "Toshko")
        self.assertEqual(animal1.gender, "male")
        self.assertEqual(animal1.weight, 30)
        self.assertEqual(animal1.life_expectancy, 180)
        self.assertEqual(animal1.food_type, "meat")
        self.assertEqual(animal1.gestation_period, 3)
        self.assertEqual(animal1.newborn, 2)
        self.assertEqual(animal1.averageWeight, 90)
        self.assertEqual(animal1.weight_age, 1.33)
        self.assertEqual(animal1.food_weight, 0.25)

    def test_animal_grow_normalWeight(self):
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        old_weight = animal1.weight
        old_age = animal1.age
        animal1.animal_grow(3)
        self.assertEqual(animal1.age, old_age + 3)
        self.assertEqual(animal1.weight, old_weight + (3 * animal1.weight_age))

    def test_animal_grow_overWeight(self):
        animal1 = Animal("Tiger", 13, "Toshko", "male", 88, 180, "meat", 3, 2, 90, 1.33, 0.25)
        animal1.animal_grow(3)
        self.assertEqual(animal1.weight, animal1.averageWeight)

    def test_animal_eat_TrueType(self):
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        food = 30 * 0.25
        shit = food / 2
        old_weight = animal1.weight
        animal1.animal_eat("meat")
        self.assertEqual(animal1.weight, old_weight + food - shit)

    def test_animal_eat_WrongType(self):
        animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        self.assertEqual(animal1.animal_eat("grass"), "Wrong food type")
        self.assertEqual(animal1.weight, 30)

    def test_animal_dead(self):
        animal1 = Animal("Tiger", 179, "Toshko", "male", 30, 180, "meat", 3, 2, 90, 1.33, 0.25)
        self.assertTrue(animal1.animal_die())

    def test_animal_alive(self):
        animal1 = Animal("Tiger", 13, "Toshko", "male", 1, 180, "meat", 3, 2, 90, 1.33, 0.25)
        self.assertFalse(animal1.animal_die())

if __name__ == '__main__':
    unittest.main()



