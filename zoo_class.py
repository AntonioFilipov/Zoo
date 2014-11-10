from animal_class import Animal
import json


class Zoo():

    def __init__(self, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    def accommodate(self, animal):
        if self.capacity > 0:
            for item in self.animals:
                if animal.species == item.species and animal.name == item.name:
                    raise ValueError("{} is already in Zoo".format(animal.name))
            self.animals.append(animal)
            self.capacity -= 1
        else:
            raise ValueError("Full zoo")

    def animals_count(self):
        count_animals = 0
        for animal in self.animals:
            count_animals += 1
        return count_animals

    def daily_incomes(self):
        return self.animals_count()*60

    def daily_outcomes(self):
        expense = 0
        for animal in self.animals:
            if animal.food_type == "meat":
                expense += animal.food_weight*4
            elif animal.food_type == "grass":
                expense += animal.food_weight*2
        return expense

    def animals_die(self):
        for animal in self.animals:
            if animal.animal_die():
                self.animals.remove(animal)

    def animal_born(self):
        reproduction = {}
        for animal in self.animals:
            if animal.species not in reproduction:
                reproduction[animal.species] = [animal.gender]
            else:
                reproduction[animal.species].append(animal.gender)

        return ""

def main():
    my_zoo = Zoo(5, 10000)
    animal1 = Animal("tiger", 13, "Toshko", "male", 30)
    animal2 = Animal("panda", 13, "Toshko", "female", 30)
    my_zoo.accommodate(animal1)
    my_zoo.accommodate(animal2)
    print(my_zoo.animals_count())
    print(my_zoo)


if __name__ == '__main__':
    main()
