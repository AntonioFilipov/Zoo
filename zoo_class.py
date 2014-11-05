from animal_class import Animal


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

