from animal_class import Animal
import json


class Zoo():
    @staticmethod
    def load(file_name):
        my_file = open(file_name, 'r')
        my_zoo = json.load(my_file)
        my_file.close()
        #result = Zoo(50, 120)
        for key in my_zoo:
            temp_animal = Animal(
                        key,
                        30,
                        "male",
                        my_zoo[key]["average_weight"],
                        my_zoo[key]["life_expectancy"],
                        my_zoo[key]["food_type"],
                        my_zoo[key]["gestation_period"],
                        my_zoo[key]["newborn"],
                        my_zoo[key]["average_weight"],
                        my_zoo[key]["food_weight"],
                        "Toshko"
                        )
            #result.animals.append(temp_animal)
        #return result
        return temp_animal


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
    zoo = Zoo(5, 10000)
    '''animal1 = Animal("Tiger", 13, "Toshko", "male", 30, 180, "grass", 3, 2, 90, 1.33, 0.25)
    animal2 = Animal("Leon", 13, "Toshko", "female", 30, 180, "grass", 3, 2, 90, 1.33, 0.25)
    animal3 = Animal("Tiger", 13, "Goshko", "female", 30, 180, "grass", 3, 2, 90, 1.33, 0.25)
    animal4 = Animal("Leon", 13, "Boshko", "female", 30, 180, "grass", 3, 2, 90, 1.33, 0.25)
    my_zoo.accommodate(animal1)
    my_zoo.accommodate(animal2)
    my_zoo.accommodate(animal3)
    my_zoo.accommodate(animal4)'''
    print(zoo.load("All_Mighty.json"))
if __name__ == '__main__':
    main()
